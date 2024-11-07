from VectorDB.client import get_chroma_client
import os 
import google.generativeai as genai
from chromadb.utils import embedding_functions
import uuid
from preprocessing import extract_text_from_pdf, chunk_text,extract_text_from_docx,extract_text_from_txt
from VectorDB.client import get_chroma_client, get_or_create_collections
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def store_document_embeddings(document_path, collection_name='document', chunk_size=5, model_name='all-mpnet-base-v2'):
    client = get_chroma_client()
    
    collection = get_or_create_collections(client, collection_name, model_name)
    sentence_trans_ef=embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2')
    _, file_extension = os.path.splitext(document_path)
    if file_extension == '.pdf':
        text = extract_text_from_pdf(document_path)
    elif file_extension == '.docx':
        text = extract_text_from_docx(document_path)
    elif file_extension == '.txt':
        text= extract_text_from_txt(document_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}. Supported types are pdf, docx, txt.")
    
    chunks = chunk_text(text, chunk_size)
    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
    metadata = [{"document": document_path, "chunk": i} for i in range(len(chunks))]
    
    collection.add(ids=ids, documents=chunks, metadatas=metadata)


def retrieve_documents(query, collection):
    
    sentence_trans_ef=embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2')
    
    results = collection.query(query_texts=[query], n_results=5,)
    return results

def generate_response(query, collection_name='document'):
    client = get_chroma_client()
    collections=client.list_collections()
    expansion_prompt = f"Expand or transform the following query to include related keywords and phrases that will improve the chances of finding relevant text in a document database:\n\nQuery: {query}\n\nExpanded query:"
    expanded_query = model.generate_content(expansion_prompt).text.strip()
    context = ""
    for collection in collections:
        documents = retrieve_documents(expanded_query,collection)
        for document in documents["documents"]:
            for i in document :
                context+=i
  
    
    prompt = f"User query: {query}\n\nRelevant information:\n{context}\n\nBased on the above information, please provide a detailed response.Dont add on your own anything just stick to the info given and answer the query without any suggestions or recommendations"
    
    chats= chat.send_message(prompt)
    # Generate the response in streaming mode
    response = chats.text
    
    print(type(chat.history[1]))
    return response
