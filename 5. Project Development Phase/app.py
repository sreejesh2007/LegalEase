from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import LegalDocumentRequest
from gemini_service import generate_legal_document
from document_generator import (
    create_txt_file,
    create_docx_file,
    create_pdf_file,
)

app = FastAPI(
    title="LegalEase",
    description="AI-Powered Legal Document Generator",
    version="1.0.0",
)

templates = Jinja2Templates(
    directory="templates"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
        },
    )


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "running",
        "application": "LegalEase",
    }


# --------------------------------------------------
# GENERATE LEGAL DOCUMENT
# --------------------------------------------------

@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    document_type: str = Form(...),
    party_a: str = Form(...),
    party_b: str = Form(...),
    effective_date: str = Form(...),
    term: str = Form(...),
    jurisdiction: str = Form(...),
    purpose: str = Form(...),
    consideration: str = Form(...),
    special_terms: str = Form(""),
    logo_text: str = Form("LegalEase"),
    font: str = Form("Arial"),
):

    data = LegalDocumentRequest(
        document_type=document_type,
        party_a=party_a,
        party_b=party_b,
        effective_date=effective_date,
        term=term,
        jurisdiction=jurisdiction,
        purpose=purpose,
        consideration=consideration,
        special_terms=special_terms,
        logo_text=logo_text,
        font=font,
    )

    try:

        draft = generate_legal_document(data)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "data": data,
                "draft": draft,
                "error": None,
            },
        )

    except Exception as exc:

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "data": data,
                "draft": "",
                "error": str(exc),
            },
        )


# --------------------------------------------------
# API GENERATE
# --------------------------------------------------

@app.post("/api/generate")
async def api_generate(data: LegalDocumentRequest):

    draft = generate_legal_document(data)

    return {
        "success": True,
        "document_type": data.document_type,
        "document": draft,
    }


# --------------------------------------------------
# EXPORT TXT
# --------------------------------------------------

@app.post("/api/export/txt")
async def export_txt(
    document_type: str = Form(...),
    party_a: str = Form(...),
    party_b: str = Form(...),
    effective_date: str = Form(...),
    term: str = Form(...),
    jurisdiction: str = Form(...),
    purpose: str = Form(...),
    consideration: str = Form(...),
    special_terms: str = Form(""),
    logo_text: str = Form("LegalEase"),
    font: str = Form("Arial"),
    draft: str = Form(...),
):

    data = LegalDocumentRequest(
        document_type=document_type,
        party_a=party_a,
        party_b=party_b,
        effective_date=effective_date,
        term=term,
        jurisdiction=jurisdiction,
        purpose=purpose,
        consideration=consideration,
        special_terms=special_terms,
        logo_text=logo_text,
        font=font,
    )

    file = create_txt_file(
        data,
        draft
    )

    return StreamingResponse(
        file,
        media_type="text/plain",
        headers={
            "Content-Disposition":
            'attachment; filename="legalease_document.txt"'
        },
    )


# --------------------------------------------------
# EXPORT DOCX
# --------------------------------------------------

@app.post("/api/export/docx")
async def export_docx(
    document_type: str = Form(...),
    party_a: str = Form(...),
    party_b: str = Form(...),
    effective_date: str = Form(...),
    term: str = Form(...),
    jurisdiction: str = Form(...),
    purpose: str = Form(...),
    consideration: str = Form(...),
    special_terms: str = Form(""),
    logo_text: str = Form("LegalEase"),
    font: str = Form("Arial"),
    draft: str = Form(...),
):

    data = LegalDocumentRequest(
        document_type=document_type,
        party_a=party_a,
        party_b=party_b,
        effective_date=effective_date,
        term=term,
        jurisdiction=jurisdiction,
        purpose=purpose,
        consideration=consideration,
        special_terms=special_terms,
        logo_text=logo_text,
        font=font,
    )

    file = create_docx_file(
        data,
        draft
    )

    return StreamingResponse(
        file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        headers={
            "Content-Disposition":
            'attachment; filename="legalease_document.docx"'
        },
    )


# --------------------------------------------------
# EXPORT PDF
# --------------------------------------------------

@app.post("/api/export/pdf")
async def export_pdf(
    document_type: str = Form(...),
    party_a: str = Form(...),
    party_b: str = Form(...),
    effective_date: str = Form(...),
    term: str = Form(...),
    jurisdiction: str = Form(...),
    purpose: str = Form(...),
    consideration: str = Form(...),
    special_terms: str = Form(""),
    logo_text: str = Form("LegalEase"),
    font: str = Form("Arial"),
    draft: str = Form(...),
):

    data = LegalDocumentRequest(
        document_type=document_type,
        party_a=party_a,
        party_b=party_b,
        effective_date=effective_date,
        term=term,
        jurisdiction=jurisdiction,
        purpose=purpose,
        consideration=consideration,
        special_terms=special_terms,
        logo_text=logo_text,
        font=font,
    )

    file = create_pdf_file(
        data,
        draft
    )

    return StreamingResponse(
        file,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            'attachment; filename="legalease_document.pdf"'
        },
    )
