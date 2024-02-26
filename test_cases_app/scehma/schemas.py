from pydantic import BaseModel

class extract_text_from_pdf(BaseModel):
    file_name : str

class chunk_document(BaseModel):
    chunk_size: int = 1000
    overlap_size : int = 150

class llm_call(BaseModel) :
    input : str
    prompt : str
