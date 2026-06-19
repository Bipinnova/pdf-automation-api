from fpdf import FPDF
import os


def create_pdf(data):

    os.makedirs("outputs", exist_ok=True)

    output_file = "outputs/output.pdf"

    pdf = FPDF(
        orientation=data.orientation,
        unit="pt",
        format=data.page_size
    )

    pdf.add_page()

    # ==========================
    # Margins
    # ==========================

    pdf.set_left_margin(data.left_margin)
    pdf.set_top_margin(data.top_margin)
    pdf.set_right_margin(data.right_margin)

    # ==========================
    # Image
    # ==========================

    if data.image_path and os.path.exists(data.image_path):

        pdf.image(
            data.image_path,
            x=data.image_x,
            y=data.image_y,
            w=data.image_width,
            h=data.image_height
        )

        pdf.set_y(
            data.image_y +
            data.image_height +
            20
        )

        pdf.set_x(
            data.left_margin
        )

    # ==========================
    # Title
    # ==========================

    pdf.set_font(
        family=data.title_font,
        style=data.title_style,
        size=data.title_size
    )

    pdf.cell(
        w=0,
        h=data.title_height,
        txt=data.title,
        align=data.title_align,
        border=data.title_border,
        ln=1
    )

    # ==========================
    # Description Heading
    # ==========================

    pdf.set_font(
        family=data.title_font,
        style="B",
        size=14
    )

    pdf.cell(
        w=0,
        h=20,
        txt="Description",
        border=0,
        ln=1
    )

    # ==========================
    # Description
    # ==========================

    pdf.set_font(
        family=data.desc_font,
        size=data.desc_size
    )

    pdf.multi_cell(
        w=0,
        h=data.desc_line_height,
        txt=data.description,
        border=data.desc_border
    )

    # ==========================
    # Dynamic Table Section
    # ==========================

    if data.table_data:

        pdf.ln(15)

        headers = list(
            data.table_data[0].keys()
        )

        total_width = (
            pdf.w
            - pdf.l_margin
            - pdf.r_margin
        )

        col_width = (
            total_width
            / len(headers)
        )

        # ----------------------
        # Table Header
        # ----------------------

        pdf.set_font(
            "Times",
            "B",
            12
        )

        for header in headers:

            pdf.cell(
                w=col_width,
                h=30,
                txt=str(header),
                border=1,
                align="C"
            )

        pdf.ln()

        # ----------------------
        # Table Rows
        # ----------------------

        pdf.set_font(
            "Times",
            "",
            12
        )

        for row in data.table_data:

            for header in headers:

                value = str(
                    row.get(
                        header,
                        ""
                    )
                )

                pdf.cell(
                    w=col_width,
                    h=25,
                    txt=value,
                    border=1
                )

            pdf.ln()

    # ==========================
    # Save PDF
    # ==========================

    pdf.output(output_file)

    return output_file