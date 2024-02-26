import chromadb
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from test_cases_app.data.config import AZURE_OPENAI_API_KEY


class VectorDB():
    vectordb=None
    def __init__(cls , collection_name):
        cls.vectordb=cls.create_db(collection_name)


    def create_db(cls , collection_name):

        if cls.vectordb is None:
            persistent_client = chromadb.PersistentClient()
            cls.vectordb= Chroma(
                client=persistent_client,
                collection_name=collection_name,
                embedding_function=OpenAIEmbeddings(api_key = AZURE_OPENAI_API_KEY))

        return cls.vectordb
    
 

    def add_one_document(self,doc):
        self.vectordb.add_documents([doc])

    def add_documents(self, docs):
        self.vectordb.add_documents(docs)


    def do_search(cls,query,k):
        docs = cls.vectordb.similarity_search(query=query, k=k)
        matching_chunks = []
        for doc, similarity in docs:
            if similarity >= 0.6:
                doc.metadata['similarity_score'] = similarity
                matching_chunks.append(doc)

        return str(matching_chunks)