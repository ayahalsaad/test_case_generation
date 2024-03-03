from fastapi import UploadFile, APIRouter, HTTPException
from typing import Union
from test_cases_app.router.router_utils import get_test_cases, get_test_cases_text
from pdfminer.high_level import extract_text_to_fp
from io import StringIO


router =APIRouter()


@router.post("/upload_file_or_insert_text/")
async def upload_file_or_provide_textual_requirements(file: Union[UploadFile] = None, text: Union[str, None] = None):
    if file is not None:
        if file.filename.endswith("pdf"):
            document = StringIO()
            extract_text_to_fp(file.file , document)
            document_as_string = document.getvalue() 
            generated_test_cases = get_test_cases(document_as_string)
            return {"test cases": generated_test_cases}
        else: 
            raise HTTPException(status_code=400, detail="Please provide a PDF file only!")
    elif text is not None:
        generated_test_cases = get_test_cases_text(text)
        return {"test cases": generated_test_cases}
    elif file is not None and text is not None:
        raise HTTPException(status_code=400, detail="Please provide either a PDF file or text, not both.")
    else:
        raise HTTPException(status_code=400, detail="No file or text provided")


