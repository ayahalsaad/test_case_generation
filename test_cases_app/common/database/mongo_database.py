from test_cases_app.data.config import MONGO_COLLECTION_NAME, MONGO_DB_NAME, MONGODB_CONNECTION_STRING
from langchain_community.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from test_cases_app.common.embeddings.azure_embeddings import embeddings
import asyncio


client = MongoClient(MONGODB_CONNECTION_STRING)
DB_NAME = MONGO_DB_NAME
COLLECTION_NAME = MONGO_COLLECTION_NAME
ATLAS_VECTOR_SEARCH_INDEX_NAME = "ayahhhh"
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]


async def add_document_to_vector_store(document):
    MONGODB_COLLECTION.delete_many({})
    vector_store = MongoDBAtlasVectorSearch.from_documents(
        document,
        embeddings,
        collection=MONGODB_COLLECTION,
    )
    query = "Return the documents that have information about the REQUIREMENTS (functional, non-functional, performance, etc.. ) of the project"
    print(vector_store.embeddings)
    matching_documents = await vector_store._similarity_search_with_score(
        query=query,
        k=20,
    )
    print(matching_documents)
    return matching_documents

async def main():
    document = ...  # Define your document here
    await add_document_to_vector_store(document)

asyncio.run(main())
