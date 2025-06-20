import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="chapters",
    embedding_function=embedding_fn
)

def store_version(text, metadata):
    try:
        collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[metadata["id"]]
        )
    except Exception as e:
        print("Error storing version:", e)


def search_version(query, n_results=5):
    try:
        return collection.query(query_texts=[query], n_results=n_results)
    except Exception as e:
        print("Search failed:", e)
        return {}
