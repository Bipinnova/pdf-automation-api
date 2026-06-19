from fastapi import FastAPI

from app.routers import (
    pdf_generator,
    pdf_extractor,
    table_extractor,
    excel_to_pdf
)

app = FastAPI(
    title="PDF Automation API",
    version="1.0"
)

app.include_router(pdf_generator.router)
app.include_router(pdf_extractor.router)
app.include_router(table_extractor.router)
app.include_router(excel_to_pdf.router)


@app.get("/")
def home():
    return {"message": "PDF Automation API Running"}