import chromadb 
from chromadb.utils import embedding_functions
def get_chroma_client():
    client = chromadb.PersistentClient(path="/media/tejas/b25dc664-2aec-424c-8f6c-f895bbec7e5d/Ericsson_RAG/data")
    return client

def get_or_create_collections(client, collection_name, model_name='all-mpnet-base-v2'):
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
    collections = client.list_collections()
    collection_names = [c.name for c in collections]
    
    if collection_name not in collection_names:
        collection = client.create_collection(name=collection_name)
    else:
        collection = client.get_collection(name=collection_name)
    return collection

def delete_all_collections():
    client = get_chroma_client()
    collections = client.list_collections()
    for collection in collections:
        client.delete_collection(collection.name)
        print(f"Deleted collection: {collection.name}")

if __name__ == '__main__':
    delete_all_collections()