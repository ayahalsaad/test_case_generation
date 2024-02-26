import PyPDF2
from langchain.prompts import PromptTemplate
from test_cases_app.prompts.requirement_extraction_prompt import requirement_extraction_prompt
from prompts.test_cases_prompts import generating_test_cases_prompt
from data.config import OPENAI_API_KEY, AZURE_ENDPOINT
from langchain.chains import LLMChain, SequentialChain
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser


requirement_prompt = PromptTemplate(template=requirement_extraction_prompt, input_variables=["document"])
prompt_test_case = PromptTemplate(template= generating_test_cases_prompt, input_variables=["text"])

output_parser = StrOutputParser()


def extract_text_from_pdf(file_name : str):
    reader = PyPDF2.PdfReader(file_name)
    with open('output.txt', 'w') as output_file:
        for page in reader.pages:
            output_file.write(page.extract_text())
        return {"status": "Text extracted successfully"}

def chunk_document(chunk_size: int = 1000, overlap_size : int = 150):
    with open('output.txt', 'r') as document:
        content = document.read()
    step = chunk_size - overlap_size
    chunks = []
    for i in range(0, len(content), step):
        chunks.append(content[i:i+chunk_size])
    return {"chunks ":chunks}

def return_text():
    with open('output.txt', 'r') as document:
        content = document.read()
        return content
    
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
    output = final_chain.run({"document" :document})
    return output["test_cases"]
