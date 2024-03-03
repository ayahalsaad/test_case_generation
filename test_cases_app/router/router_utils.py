from test_cases_app.utils import chunk_document, get_relevant_documents_by_FAISS, generate_test_cases

def get_test_cases(content : str):
    chunks = chunk_document(content)
    matching_chunks = get_relevant_documents_by_FAISS(chunks)
    generated_test_cases = generate_test_cases(matching_chunks)
    return generated_test_cases


def get_test_cases_text(text: str):
    document = text
    generated_test_cases = generate_test_cases(document)
    return {"test cases": generated_test_cases}
