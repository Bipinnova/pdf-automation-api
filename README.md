# PDF Automation API

## Overview

PDF Automation API is a FastAPI-based application that provides multiple PDF processing capabilities through REST APIs.

The project is designed using a layered architecture and supports:

* Dynamic PDF Generation
* PDF Text Extraction
* PDF Table Extraction
* Excel to PDF Conversion
* File Upload & Processing
* Reusable PDF Components

This project demonstrates how to build scalable backend services using FastAPI, Pydantic, and Python libraries such as FPDF, PyMuPDF, Pandas, and Tabula.

---

# Features

## 1. Dynamic PDF Generation

Generate custom PDF documents using JSON input.

Supported Components:

* Headings
* Paragraphs
* Images
* Tables
* Bullet Lists
* Dynamic Content

Example Use Cases:

* Resume Generator
* Invoice Generator
* Reports
* Certificates
* Product Catalogs
* Employee Profiles

---

## 2. PDF Text Extraction

Extract text from uploaded PDF files using PyMuPDF.

Workflow:

PDF → Text Extraction → JSON Response

---

## 3. PDF Table Extraction

Extract tables from PDF files and convert them into:

* CSV
* Excel

Workflow:

PDF → Table Detection → CSV / XLSX

---

## 4. Excel to PDF Conversion

Read Excel files using Pandas and generate PDF documents automatically.

Workflow:

Excel → Read Rows → Generate PDFs

---

# Project Architecture

```text
                Client
                  |
                  |
          (Swagger/Postman)
                  |
                  v
          FastAPI Endpoint
                  |
                  v
              Router
                  |
                  v
          Request Validation
             (Pydantic)
                  |
                  v
              Service
       (Business Logic Layer)
                  |
                  v
      PDF / Excel / Table Logic
                  |
                  v
          File Generation
                  |
                  v
         outputs/ Directory
                  |
                  v
          API Response
```

---

# Folder Structure

```text
pdf_automation_api/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── pdf_generator.py
│   │   ├── pdf_extractor.py
│   │   ├── table_extractor.py
│   │   └── excel_to_pdf.py
│   │
│   ├── schemas/
│   │   └── pdf_schema.py
│   │
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── extract_service.py
│   │   ├── table_service.py
│   │   └── excel_service.py
│   │
│   └── utils/
│       └── file_handler.py
│
├── uploads/
│
├── outputs/
│
├── requirements.txt
│
└── README.md
```

---

# Workflow Explanation

## main.py

Application entry point.

Responsibilities:

* Create FastAPI instance
* Register routers
* Start application

---

## routers/

Responsible for handling HTTP requests.

Examples:

* POST /pdf/generate
* POST /extract/text
* POST /table/extract
* POST /excel/generate-pdfs

Responsibilities:

* Receive request
* Validate request
* Call service layer
* Return response

---

## schemas/

Responsible for request validation.

Uses:

* Pydantic Models

Responsibilities:

* Validate incoming data
* Enforce required fields
* Return 422 errors for invalid requests

---

## services/

Contains all business logic.

### pdf_service.py

Responsible for:

* PDF generation
* Dynamic content rendering
* Table rendering
* Image rendering

Uses:

* FPDF2

---

### extract_service.py

Responsible for:

* Extracting text from PDFs

Uses:

* PyMuPDF

---

### table_service.py

Responsible for:

* Extracting tables from PDFs
* Exporting CSV files
* Exporting Excel files

Uses:

* tabula-py

---

### excel_service.py

Responsible for:

* Reading Excel files
* Generating PDF documents from rows

Uses:

* Pandas
* FPDF2

---

## uploads/

Stores uploaded files temporarily.

Examples:

* PDF files
* Images
* Excel files

---

## outputs/

Stores generated files.

Examples:

* output.pdf
* output.csv
* output.xlsx

---

# API Endpoints

## Generate PDF

```http
POST /pdf/generate
```

Generate dynamic PDF documents.

---

## Extract Text From PDF

```http
POST /extract/text
```

Extract text from uploaded PDFs.

---

## Extract Tables From PDF

```http
POST /table/extract
```

Extract tables and export to CSV/Excel.

---

## Generate PDFs From Excel

```http
POST /excel/generate-pdfs
```

Generate multiple PDF documents from Excel rows.

---

# Installation

Clone Repository

```bash
git clone https://github.com/Bipinnova/pdf-automation-api.git
```

Move Into Project

```bash
cd pdf-automation-api
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Project

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Technologies Used

Backend

* Python
* FastAPI

PDF Processing

* FPDF2
* PyMuPDF
* tabula-py

Data Processing

* Pandas
* OpenPyXL

Validation

* Pydantic

API Documentation

* Swagger UI

---

# Future Enhancements

* Header & Footer Support
* Page Numbering
* Watermark Support
* QR Code Generation
* Barcode Generation
* HTML to PDF Conversion
* Word to PDF Conversion
* PDF Encryption
* PDF Merging
* PDF Splitting
* Cloud Storage Integration
* Authentication & Authorization

---

# Author

Bipin Yadav

Python Backend Developer | FastAPI Developer | AI Application Developer
