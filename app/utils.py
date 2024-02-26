import PyPDF2
from openai import OpenAI
from app.data.config import OPEN_AI_KEY


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

        
def llm_call(input : str , prompt : str):
    client = OpenAI(api_key=OPEN_AI_KEY)
    if not client.api_key:
        raise Exception("Please set your OpenAI API key as an environment variable.")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input},
        ],
    )
    generated_llm_answer = response.choices[0].message.content
    return str(generated_llm_answer)
