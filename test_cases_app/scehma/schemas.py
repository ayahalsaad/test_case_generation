from pydantic import BaseModel
from typing import List, Optional
from fastapi import UploadFile
import humps


def to_camel(string: str) -> str:
    return humps.camelize(string)

def to_snake(string: str) -> str:
    return humps.decamelize(string)


class GenerateTestCasesInput(BaseModel):
    file: Optional[UploadFile] = None
    text: Optional[str] = None


class GenerateTestCasesOutput(BaseModel):
    test_cases: List[str]

print (to_camel("ayah_alsaad"))