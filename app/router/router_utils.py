from app.utils import extract_text_from_pdf, chunk_document, llm_call
from app.common.database.database import VectorDB
from app.prompts.requirement_extraction_prompts import requirement_extraction_prompt
from app.prompts.test_cases_prompts import generating_test_cases_prompt
from app.prompts.database_query_file import requirement_query




def write_file_locally(file_location, file):
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    return {"status": "File uploaded successfully", "file_location": file_location}


def get_extracted_requirements(vector_db: VectorDB ,file_name : str , chunk_size: int = 1000, overlap_size : int = 150):
    extract_text_from_pdf(file_name)
    vector_db.add_one_document({"file_name": file_name})

    chunks = chunk_document(chunk_size, overlap_size)
    documents = [{"text": chunk, "metadata": {}} for chunk in chunks["chunks"]]
    vector_db.add_documents(docs=documents)
    matching_chunks = vector_db.do_search(query=requirement_query, k=30)
    client_requirements = llm_call(input= matching_chunks, prompt= requirement_extraction_prompt)
    return client_requirements

def get_test_cases(extracted_requirements=None):
    generated_test_cases = llm_call(input = extracted_requirements, prompt = generating_test_cases_prompt)
    return {"test cases": generated_test_cases}

