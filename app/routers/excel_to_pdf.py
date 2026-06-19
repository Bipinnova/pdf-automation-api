from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.excel_service import generate_pdfs_from_excel

router = APIRouter(
    prefix="/excel",
    tags=["Excel To PDF"]
)


@router.post("/generate-pdfs")
async def excel_to_pdf(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    pdfs = generate_pdfs_from_excel(
        file_path
    )

    return {
        "generated_files": pdfs
    }