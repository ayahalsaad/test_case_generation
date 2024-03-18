from typing import AsyncIterable, Awaitable
from test_cases_app.utils.utils import chunk_document, get_relevant_documents_by_FAISS
from test_cases_app.utils.llm_utils import generate_test_cases, azure_llm
from pdfminer.high_level import extract_text_to_fp
from io import StringIO
from langchain.callbacks import AsyncIteratorCallbackHandler
import asyncio
from typing import Any


async def send_message(input_data: str, input_type: str) -> AsyncIterable[Any]:
    funcs = {
        "file": get_test_cases,
        "text": get_test_cases_text,
    }

    callback = AsyncIteratorCallbackHandler()
    model = azure_llm(callbacks=[callback])

    async def wrap_done(fn: Awaitable, event: asyncio.Event):
        try:
            await fn
        except Exception as e:
            print(f"Caught exception: {e}")
        finally:
            event.set()

    task = asyncio.create_task(
        wrap_done(
            funcs[input_type](model, input_data, callback),
            callback.done,
        ),
    )
    async for token in callback.aiter():
        print(token)
        yield token

    await task


def get_text(file) -> str:
    document = StringIO()
    extract_text_to_fp(file, document)
    document_as_string = document.getvalue()
    return document_as_string


async def get_test_cases(llm, content: str, callback) -> str:
    chunks = chunk_document(content)
    matching_chunks = get_relevant_documents_by_FAISS(chunks)
    generated_test_cases = await generate_test_cases(llm, matching_chunks, callback)
    return generated_test_cases


async def get_test_cases_text(llm, text: str, callback) -> str:
    document = text
    generated_test_cases = await generate_test_cases(llm, document, callback)
    return generated_test_cases
