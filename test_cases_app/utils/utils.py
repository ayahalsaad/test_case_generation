from langchain_community.vectorstores.faiss import FAISS
from test_cases_app.common.embeddings.azure_embeddings import get_azure_embeddings
from langchain_core.documents import Document
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_document(
    content: str, chunk_size: int = 1500, overlap_size: int = 150
) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=overlap_size
    )
    chunks = text_splitter.split_text(content)
    documents = []
    for i, chunk in enumerate(chunks):
        metadata = {"chunk_id": i + 1, "total_chunks": len(chunks)}
        documents.append(Document(page_content=chunk, metadata=metadata))

    return documents


def get_relevant_documents_by_FAISS(documents) -> List[Document]:
    db = FAISS.from_documents(documents, get_azure_embeddings())
    query = "Return the documents that have information about the PROJECT'S REQUIREMENTS (functional, non-functional, performance, etc.. ) of the project."
    matching_documents = db.similarity_search(query=query, k=20)
    return matching_documents

