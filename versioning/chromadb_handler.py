import chromadb

client = chromadb.PersistentClient(path="./chroma_store")

collection = client.get_or_create_collection(name="chapters")

def store_version(text, metadata):
    try:
        print(f"📦 Storing version with metadata: {metadata}")
        collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[metadata["id"]]
        )
    except Exception as e:
        print("❌ Error storing version:", e)


def search_version(query, n_results=5):
    try:
        return collection.query(query_texts=[query], n_results=n_results)
    except Exception as e:
        print("Search failed:", e)
        return {}
