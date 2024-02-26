import os 
from fastapi import UploadFile, APIRouter
from app.common.database.database import VectorDB
from app.router.router_utils import write_file_locally, get_extracted_requirements, get_test_cases
router=APIRouter()


vector_db = VectorDB(collection_name="test_cases")

@router.post("/upload_file/")
async def upload_file(file: UploadFile):
    file_location = os.path.join("uploads", file.filename)
    write_file_locally(file_location, file)
    requirements = get_extracted_requirements(vector_db, file_name=file_location)
    generated_test_cases = get_test_cases(extracted_requirements=requirements)
    return  {"file name: ": file.filename , "test cases": generated_test_cases}

