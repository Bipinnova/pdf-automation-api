from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.extract_service import extract_text_from_pdf

router = APIRouter(
    prefix="/extract",
    tags=["PDF Text Extraction"]
)


@router.post("/text")
async def extract_text(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "text": text
    }