from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from gemini_service import build_legal_document
from document_generator import create_txt, create_docx, create_pdf


app = FastAPI(
    title="LegalEase",
    description="AI-Powered Legal Document Generator",
    version="1.0"
)


templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate_document_page(
    request: Request,
    document_type: str = Form(...),
    details: str = Form(...)
):
    try:
        if not details.strip():
            raise ValueError(
                "Please enter the required document details."
            )

        document = build_legal_document(
            document_type,
            details
        )

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "document_type": document_type,
                "document": document
            }
        )

    except Exception as error:

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "document_type": document_type,
                "document": "",
                "error": str(error)
            }
        )


@app.post("/export/txt")
async def export_txt(
    document: str = Form(...)
):
    data = create_txt(document)

    return Response(
        content=data,
        media_type="text/plain",
        headers={
            "Content-Disposition":
            "attachment; filename=legalease_document.txt"
        }
    )


@app.post("/export/docx")
async def export_docx(
    document: str = Form(...)
):
    data = create_docx(document)

    return Response(
        content=data,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        headers={
            "Content-Disposition":
            "attachment; filename=legalease_document.docx"
        }
    )


@app.post("/export/pdf")
async def export_pdf(
    document: str = Form(...)
):
    data = create_pdf(document)

    return Response(
        content=data,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=legalease_document.pdf"
        }
    )


@app.get("/health")
async def health():
    return {
        "status": "running",
        "application": "LegalEase"
    }
