import os 
from fastapi import UploadFile, APIRouter, HTTPException
from typing import Optional
from test_cases_app.router.router_utils import get_test_cases_files, get_test_cases_text, write_string_to_file
from pdfminer.high_level import extract_text
router=APIRouter()


@router.post("/upload_file_or_insert_text/")
async def upload_file(file: Optional[UploadFile] , text: Optional[str]):
    if file is not None:
        content = extract_text(file.filename)
        write_string_to_file(content)
        generated_test_cases = get_test_cases_files(file.filename)
        return  {"file name: ": file.filename , "test cases": generated_test_cases}
    elif text is not None:
        generated_test_cases = get_test_cases_text(text)
        return {"test cases": generated_test_cases}
    else:
        raise HTTPException(status_code=400, detail="No file or text provided")

