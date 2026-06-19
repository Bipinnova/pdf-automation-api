from fastapi import APIRouter

from app.schemas.pdf_schema import PDFRequest
from app.services.pdf_service import create_pdf

router = APIRouter(
    prefix="/pdf",
    tags=["PDF Generator"]
)


@router.post("/generate")
def generate_pdf(data: PDFRequest):

    file_name = create_pdf(data)

    return {
        "message": "PDF Generated Successfully",
        "file": file_name
    }