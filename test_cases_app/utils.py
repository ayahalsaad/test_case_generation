from langchain.prompts import PromptTemplate
from test_cases_app.prompts.requirement_extraction_prompt import requirement_extraction_prompt
from test_cases_app.prompts.test_cases_prompt import generating_test_cases_prompt
from langchain.chains import LLMChain, SequentialChain
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
from langchain_community.vectorstores.faiss import FAISS
from test_cases_app.common.embeddings.azure_embeddings import embeddings
from test_cases_app.data.config import AZURE_ENDPOINT, OPENAI_API_KEY
from langchain_core.documents import Document
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter


requirement_prompt = PromptTemplate(template=requirement_extraction_prompt, input_variables=["document"])
prompt_test_case = PromptTemplate(template= generating_test_cases_prompt, input_variables=["text"])
output_parser = StrOutputParser()


def chunk_document(content: str, chunk_size: int = 1500, overlap_size: int = 150) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap_size)
    chunks = text_splitter.split_text(content)
    documents = []
    for i, chunk in enumerate(chunks):
        metadata = {
            "chunk_id": i + 1,
            "total_chunks": len(chunks)
        }
        documents.append(Document(page_content=chunk, metadata=metadata))
        
    return documents
 
def get_relevant_documents_by_FAISS(documents):
    db = FAISS.from_documents(documents, embeddings)
    query = "Return the documents that have information about the PROJECT'S REQUIREMENTS (functional, non-functional, performance, etc.. ) of the project."
    matching_documents = db.similarity_search_with_relevance_scores(query=query, k=10)
    return matching_documents


def azure_llm_calling():
    azure_llm = AzureChatOpenAI(
        deployment_name="aya12344",
        azure_endpoint = AZURE_ENDPOINT, 
        openai_api_key=OPENAI_API_KEY,  
        api_version="2024-02-15-preview",
        temperature=0,
        model="gpt-4",

    )
    return azure_llm

def generate_test_cases(document):
    requirement_chain = LLMChain(llm=azure_llm_calling(), prompt= requirement_prompt, verbose=True, output_parser= output_parser ,output_key="requirements")
    test_case_chain = LLMChain(llm=azure_llm_calling(), prompt= prompt_test_case, verbose=True, output_parser= output_parser,output_key="test_cases")
    final_chain = SequentialChain(
        chains=[ requirement_chain, test_case_chain], input_variables=["document"],verbose=True, output_variables= ["test_cases"])
    output = final_chain.invoke({"document" :document})
    return output

