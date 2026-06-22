import os
import tabula
import pandas as pd


def extract_table(pdf_path):

    # Create outputs folder if not exists
    os.makedirs("outputs", exist_ok=True)

    # Extract all tables from all pages
    tables = tabula.read_pdf(
        pdf_path,
        pages="all",
        multiple_tables=True
    )

    if not tables:
        return {
            "message": "No tables found in PDF"
        }

    excel_path = "outputs/all_tables.xlsx"

    csv_files = []

    with pd.ExcelWriter(excel_path) as writer:

        for index, table in enumerate(tables, start=1):

            csv_path = f"outputs/table_{index}.csv"

            # Save CSV
            table.to_csv(
                csv_path,
                index=False
            )

            csv_files.append(csv_path)

            # Save Excel Sheet
            table.to_excel(
                writer,
                sheet_name=f"Table_{index}",
                index=False
            )

    return {
        "total_tables": len(tables),
        "csv_files": csv_files,
        "excel_file": excel_path
    }