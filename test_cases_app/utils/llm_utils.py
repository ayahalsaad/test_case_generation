from langchain.chains import LLMChain, SequentialChain
from langchain_openai import AzureChatOpenAI
from config import AZURE_ENDPOINT, OPENAI_API_KEY, AZURE_DEPLOYMENT_NAME
from langchain_core.output_parsers import StrOutputParser


from test_cases_app.templates.requirement_extraction import (
    get_requirement_prompt,
)
from test_cases_app.templates.test_cases import (
    get_test_cases_prompt,
)

output_parser = StrOutputParser()


def azure_llm(callbacks: list) -> AzureChatOpenAI:
    azure_llm = AzureChatOpenAI(
        deployment_name=AZURE_DEPLOYMENT_NAME,
        azure_endpoint=AZURE_ENDPOINT,
        openai_api_key=OPENAI_API_KEY,
        api_version="2024-02-15-preview",
        temperature=0,
        model="gpt-4",
        streaming=True,
        callbacks=callbacks,
    )
    return azure_llm


async def get_chain(llm, prompt, output_key) -> LLMChain:
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        output_parser=output_parser,
        output_key=output_key,
        verbose=True,
    )
    return chain


async def generate_test_cases(llm, document, callback):
    requirement_chain = await get_chain(
        llm=azure_llm([]), prompt=get_requirement_prompt(), output_key="requirements"
    )
    test_case_chain = await get_chain(
        llm=azure_llm(callbacks=[callback]),
        prompt=get_test_cases_prompt(),
        output_key="test_cases",
    )

    final_chain = SequentialChain(
        chains=[requirement_chain, test_case_chain],
        input_variables=["document"],
        output_variables=["test_cases"],
    )
    output = await final_chain.ainvoke({"document": document})

    return output["test_cases"]

