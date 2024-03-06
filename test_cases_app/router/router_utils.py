from typing import AsyncIterable
from test_cases_app.utils.utils import chunk_document, get_relevant_documents_by_FAISS
from test_cases_app.utils.llm_utils import generate_test_cases
from pdfminer.high_level import extract_text_to_fp
from io import StringIO


def get_text(file) -> str:
    document = StringIO()
    extract_text_to_fp(file, document)
    document_as_string = document.getvalue()
    return document_as_string


async def get_test_cases(content: str) -> str:
    chunks = chunk_document(content)
    matching_chunks = get_relevant_documents_by_FAISS(chunks)
    generated_test_cases = await generate_test_cases(matching_chunks)
    return generated_test_cases


async def get_test_cases_text(text: str) -> str:
    document = text
    generated_test_cases = await generate_test_cases(document)
    return generated_test_cases


async def send_message(document: str) -> AsyncIterable[str]:
    generated_test_cases = await get_test_cases(document)

    for test_case in generated_test_cases:
        yield f"data: {test_case}\n\n"


async def send_message_text(text: str) -> AsyncIterable[str]:
    generated_test_cases = await get_test_cases_text(text)

    for test_case in generated_test_cases:
        yield f"data: {test_case}\n\n"


