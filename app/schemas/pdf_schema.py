from pydantic import BaseModel
from typing import List, Dict, Any


class PDFRequest(BaseModel):

    title: str
    description: str

    table_data: List[Dict[str, Any]] = []

    orientation: str = "P"
    page_size: str = "A4"

    image_path: str = ""

    image_width: int = 80
    image_height: int = 50

    image_x: int = 10
    image_y: int = 10

    title_font: str = "Times"
    title_style: str = "B"
    title_size: int = 24

    title_align: str = "C"
    title_height: int = 50
    title_border: int = 0

    desc_font: str = "Times"
    desc_size: int = 12
    desc_line_height: int = 15
    desc_border: int = 0

    left_margin: int = 10
    top_margin: int = 10
    right_margin: int = 10