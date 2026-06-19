from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.table_service import extract_table

router = APIRouter(
    prefix="/table",
    tags=["Table Extraction"]
)


@router.post("/extract")
async def table_extract(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = extract_table(file_path)

    return result