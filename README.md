# PDF Automation API

## Overview

PDF Automation API is a reusable and scalable FastAPI-based application that generates dynamic PDF documents from JSON input.

Unlike traditional PDF generators that are built for a single use case, this project follows a generic content-driven approach that allows users to create different types of PDFs such as:

* Resumes
* Invoices
* Reports
* Certificates
* Product Catalogs
* Employee Profiles
* Educational Documents
* Research Papers
* Animal Information Sheets
* Custom PDF Documents

The API receives structured JSON data and converts it into professionally formatted PDF documents.

---

## Features

### Dynamic PDF Generation

Generate PDF documents using API requests.

### Heading Support

Create section titles with configurable:

* Font Family
* Font Size
* Bold
* Italic
* Underline
* Alignment

### Paragraph Support

Add large blocks of text with automatic wrapping.

### Bullet Lists

Generate ordered and unordered content sections.

### Dynamic Tables

Create tables with:

* Dynamic Columns
* Dynamic Rows
* Auto Width Calculation
* Custom Data

### Image Support

Insert images with:

* Custom Width
* Custom Height
* Position Control

### Formatting Options

Control:

* Page Orientation
* Page Size
* Margins
* Font Styles
* Alignment

### Reusable Architecture

The same API can generate multiple document types without changing the code.

---

## Project Structure

```text
pdf_automation_api/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── routers/
│   │   └── pdf_generator.py
│   │
│   ├── schemas/
│   │   └── pdf_schema.py
│   │
│   ├── services/
│   │   └── pdf_service.py
│   │
│   └── utils/
│       └── pdf_helpers.py
│
├── uploads/
├── outputs/
│
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Backend

* Python
* FastAPI

### PDF Generation

* FPDF2

### Data Validation

* Pydantic

### API Documentation

* Swagger UI

---

## API Workflow

```text
Client
   |
   v

FastAPI Endpoint

   |
   v

Request Validation (Pydantic)

   |
   v

PDF Service Layer

   |
   v

FPDF Engine

   |
   v

Generated PDF

   |
   v

Response
```

---

## Example Use Cases

### Resume Generator

Generate professional resumes dynamically.

### Invoice Generator

Generate customer invoices using JSON data.

### Certificate Generator

Generate training and achievement certificates.

### Report Generator

Generate business and analytical reports.

### Product Catalog Generator

Generate catalogs containing images and descriptions.

---

## API Endpoint

### Generate PDF

```http
POST /pdf/generate
```

---

## Sample Request

```json
{
  "title": "Employee Profile",

  "elements": [

    {
      "type": "heading",
      "text": "Personal Information",
      "font_size": 18,
      "bold": true
    },

    {
      "type": "paragraph",
      "text": "Employee details and profile information."
    },

    {
      "type": "table",
      "table": {
        "headers": [
          "Field",
          "Value"
        ],
        "rows": [
          [
            "Name",
            "John Doe"
          ],
          [
            "Department",
            "IT"
          ]
        ]
      }
    }
  ]
}
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/your-username/pdf-automation-api.git
```

Move into project:

```bash
cd pdf-automation-api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

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

## Future Enhancements

* Header & Footer Support
* Page Numbering
* Watermark Support
* QR Code Generation
* Barcode Generation
* HTML to PDF
* Excel to PDF
* Word to PDF
* Digital Signatures
* PDF Encryption
* PDF Merging
* PDF Splitting
* Cloud Storage Integration

---

## Author

Bipin Yadav

Python Backend Developer | FastAPI Developer | AI Application Developer
