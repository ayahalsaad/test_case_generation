from fastapi import UploadFile, APIRouter, HTTPException
from typing import Union
from fastapi.responses import StreamingResponse
from test_cases_app.router.router_utils import (
    get_text,
    send_message,
    send_message_text,
)


router = APIRouter()


@router.post("/upload")
async def upload_file_or_provide_text_requirements(
    file: Union[UploadFile] = None, text: Union[str, None] = None
) -> dict[str, str]:
    if file is None and text is None:
        raise HTTPException(status_code=400, detail="No PDF file or text provided")
    if file is not None and text is not None:
        raise HTTPException(
            status_code=400,
            detail="Please provide either a PDF file or text, not both.",
        )
    if file is not None:
        if file.filename.endswith("pdf"):
            document = get_text(file.file)
            return StreamingResponse(
                send_message(document), media_type="text/event-stream"
            )
        else:
            raise HTTPException(
                status_code=400, detail="Please provide a PDF file only!"
            )
    if text is not None:
        return StreamingResponse(
            send_message_text(text), media_type="text/event-stream"
        )
