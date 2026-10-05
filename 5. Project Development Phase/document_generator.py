from io import BytesIO
from docx import Document
from docx.shared import Pt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_txt(document_text):
    return document_text.encode("utf-8")


def create_docx(document_text):
    document = Document()

    title = document.add_heading(
        "LegalEase - Legal Document Draft",
        level=1
    )

    for paragraph in document_text.split("\n"):
        if paragraph.strip():
            p = document.add_paragraph(paragraph)
            p.style.font.name = "Arial"
            p.style.font.size = Pt(11)

    output = BytesIO()
    document.save(output)
    output.seek(0)

    return output.getvalue()


def create_pdf(document_text):
    output = BytesIO()

    pdf = SimpleDocTemplate(
        output,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(
            "LegalEase - Legal Document Draft",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 15))

    for paragraph in document_text.split("\n"):
        if paragraph.strip():
            safe_text = (
                paragraph
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            story.append(
                Paragraph(
                    safe_text,
                    styles["BodyText"]
                )
            )

            story.append(Spacer(1, 8))

    pdf.build(story)

    output.seek(0)

    return output.getvalue()
