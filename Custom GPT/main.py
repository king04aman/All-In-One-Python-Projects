import os
import openai
import sys
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma


os.environ["OPENAI_API_KEY"] = "your_api_key_here"
PERSIST = False

query = sys.argv[1] if len(sys.argv) > 1 else None

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader]) if PERSIST else VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []

while True:
    if not query:
        query = input("Prompt (type 'quit' to exit): ")
    if query.lower() in ['quit', 'q', 'exit']:
        print("Exiting the program...")
        sys.exit()
    
    result = chain({"question": query, "chat_history": chat_history})
    
    print("Response:", result['answer'])

    chat_history.append((query, result['answer']))
    query = None 
