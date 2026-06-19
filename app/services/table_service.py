import tabula


def extract_table(pdf_path):

    tables = tabula.read_pdf(
        pdf_path,
        pages="1"
    )

    csv_path = "outputs/output.csv"
    excel_path = "outputs/output.xlsx"

    tables[0].to_csv(
        csv_path,
        index=False
    )

    tables[0].to_excel(
        excel_path,
        index=False
    )

    return {
        "csv": csv_path,
        "excel": excel_path
    }