import pandas as pd
from fpdf import FPDF


def generate_pdfs_from_excel(
    excel_path
):

    df = pd.read_excel(
        excel_path
    )

    generated_files = []

    for _, row in df.iterrows():

        pdf = FPDF()
        pdf.add_page()

        pdf.set_font(
            "Times",
            "B",
            24
        )

        pdf.cell(
            0,
            20,
            str(row["name"]),
            align="C",
            new_x="LMARGIN",
            new_y="NEXT"
        )

        for column in df.columns[1:]:

            pdf.set_font(
                "Times",
                "B",
                12
            )

            pdf.cell(
                50,
                10,
                f"{column}:"
            )

            pdf.set_font(
                "Times",
                size=12
            )

            pdf.cell(
                50,
                10,
                str(row[column]),
                new_x="LMARGIN",
                new_y="NEXT"
            )

        pdf_file = f"outputs/{row['name']}.pdf"

        pdf.output(pdf_file)

        generated_files.append(
            pdf_file
        )

    return generated_files