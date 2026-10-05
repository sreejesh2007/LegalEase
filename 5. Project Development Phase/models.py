from typing import Literal

from pydantic import BaseModel


DocumentType = Literal[
    "Non-Disclosure Agreement (NDA)",
    "Employment Agreement",
    "Lease Agreement",
    "Service Agreement",
    "General Agreement",
]

FontType = Literal[
    "Arial",
    "Georgia",
    "Times New Roman",
    "Courier New",
]


class LegalDocumentRequest(BaseModel):
    document_type: DocumentType
    party_a: str
    party_b: str
    effective_date: str
    term: str
    jurisdiction: str
    purpose: str
    consideration: str
    special_terms: str = ""
    logo_text: str = "LegalEase"
    font: FontType = "Arial"
