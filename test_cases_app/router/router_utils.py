from test_cases_app.utils import extract_text_from_pdf, chunk_document, generate_test_cases
from test_cases_app.common.database.database import VectorDB
from test_cases_app.prompts.database_query_file import requirement_query


def write_string_to_file(content: str):
    with open("output.txt", 'w') as content_file:
        content_file.write(content)

def get_test_cases_files(vector_db: VectorDB ,file_name : str , chunk_size: int = 1000, overlap_size : int = 150):
    extract_text_from_pdf(file_name)
    vector_db.add_one_document({"file_name": file_name}) #needs fixing
    chunks = chunk_document(chunk_size, overlap_size) #needs fixing
    documents = [{"text": chunk, "metadata": {}} for chunk in chunks["chunks"]] #needs fixing
    vector_db.add_documents(docs=documents) #needs fixing
    matching_chunks = vector_db.do_search(query=requirement_query, k=30) #needs fixing
    generated_test_cases = generate_test_cases(matching_chunks)
    return {"test cases": generated_test_cases}


def get_test_cases_text(text: str):
    document = text
    generated_test_cases = generate_test_cases(document)
    return {"test cases": generated_test_cases}
