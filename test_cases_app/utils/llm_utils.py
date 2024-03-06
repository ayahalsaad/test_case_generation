from typing import AsyncIterable
from langchain.chains import LLMChain, SequentialChain
from langchain_openai import AzureChatOpenAI
from config import AZURE_ENDPOINT, OPENAI_API_KEY, AZURE_DEPLOYMENT_NAME
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks import AsyncIteratorCallbackHandler

from test_cases_app.prompts.requirement_extraction_prompt import (
    get_requirement_prompt,
)
from test_cases_app.prompts.test_cases_prompt import (
    get_test_cases_prompt,
)

output_parser = StrOutputParser()
streaming_handler = AsyncIteratorCallbackHandler()


def azure_llm() -> AzureChatOpenAI:
    azure_llm = AzureChatOpenAI(
        deployment_name=AZURE_DEPLOYMENT_NAME,
        azure_endpoint=AZURE_ENDPOINT,
        openai_api_key=OPENAI_API_KEY,
        api_version="2024-02-15-preview",
        temperature=0,
        model="gpt-4",
        streaming=True,
        verbose=True,
        callbacks=[streaming_handler],
    )
    return azure_llm


async def call_chain(llm, prompt, output_key) -> LLMChain:
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        output_parser=output_parser,
        output_key=output_key,
    )
    return chain


async def generate_test_cases(document) -> str:
    requirement_chain = await call_chain(
        llm=azure_llm(), prompt=get_requirement_prompt(), output_key="requirements"
    )
    test_case_chain = await call_chain(
        llm=azure_llm(), prompt=get_test_cases_prompt(), output_key="test_cases"
    )

    final_chain = SequentialChain(
        chains=[requirement_chain, test_case_chain],
        input_variables=["document"],
        verbose=True,
        output_variables=["test_cases"],
    )
    output = await final_chain.ainvoke({"document": document})
    return output["test_cases"]
