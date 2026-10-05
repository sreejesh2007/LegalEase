import os
from google import genai


DEFAULT_MODEL = "gemini-3.8-flash"

FALLBACK_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
]


def generate_legal_document(data):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Gemini API key is not configured. "
            "Please add GEMINI_API_KEY as an environment variable or secret."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an AI assistant helping create a legal document draft.

IMPORTANT:
- Generate a professional legal document draft.
- Do not claim that the document is legally guaranteed or legally valid.
- Do not invent specific laws, statutes, court cases, or legal citations.
- Clearly structure the document with headings and clauses.
- Use the information supplied by the user.
- If important legal information is missing, use a reasonable placeholder or state that professional legal review is required.
- The output is a draft and not legal advice.

DOCUMENT TYPE:
{data.document_type}

PARTY A:
{data.party_a}

PARTY B:
{data.party_b}

EFFECTIVE DATE:
{data.effective_date}

TERM:
{data.term}

JURISDICTION:
{data.jurisdiction}

PURPOSE / ROLE / PROPERTY:
{data.purpose}

PAYMENT / CONSIDERATION:
{data.consideration}

SPECIAL TERMS:
{data.special_terms}

Create a complete, well-structured legal document draft.

Include:
1. Document title
2. Introduction / parties
3. Purpose
4. Definitions where appropriate
5. Main terms and obligations
6. Payment or consideration where applicable
7. Confidentiality where applicable
8. Term and termination
9. Dispute resolution where appropriate
10. Governing law
11. General provisions
12. Signature section

End with:

LEGAL REVIEW NOTICE:
This document is an AI-generated draft and should be reviewed by a qualified legal professional before actual use.
"""

    errors = []

    models_to_try = []

    preferred_model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
    models_to_try.append(preferred_model)

    for model in FALLBACK_MODELS:
        if model not in models_to_try:
            models_to_try.append(model)

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )

            text = getattr(response, "text", None)

            if text and text.strip():
                return text.strip()

            errors.append(f"{model_name}: Empty response")

        except Exception as exc:
            errors.append(f"{model_name}: {str(exc)}")

    raise RuntimeError(
        "Gemini document generation failed. "
        + " | ".join(errors)
    )
