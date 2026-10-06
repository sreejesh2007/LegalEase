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
            "Please add GEMINI_API_KEY as a Codespaces secret."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an AI assistant helping create a legal document draft.

Create a professional, clearly structured legal document based on
the information provided below.

IMPORTANT:
- This is an AI-generated draft.
- Do not claim that the document is guaranteed to be legally valid.
- Do not invent laws, statutes, court cases, or legal citations.
- Do not provide false legal guarantees.
- Use the information provided by the user.
- If important legal information is missing, indicate that professional
  legal review is required.
- Use clear headings and clauses.
- Include a signature section.

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

Create the complete document draft.

Include appropriate sections such as:

1. Title
2. Parties
3. Purpose
4. Definitions, if required
5. Main terms and obligations
6. Payment or consideration, if applicable
7. Confidentiality, if applicable
8. Term and termination
9. Governing law
10. General provisions
11. Signature section

At the end include this notice:

LEGAL REVIEW NOTICE:
This document is an AI-generated draft and should be reviewed by
a qualified legal professional before actual use.
"""

    preferred_model = os.getenv(
        "GEMINI_MODEL",
        DEFAULT_MODEL
    )

    models_to_try = [preferred_model]

    for model in FALLBACK_MODELS:
        if model not in models_to_try:
            models_to_try.append(model)

    errors = []

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )

            generated_text = getattr(
                response,
                "text",
                None
            )

            if generated_text and generated_text.strip():
                return generated_text.strip()

            errors.append(
                f"{model_name}: Empty response"
            )

        except Exception as exc:
            errors.append(
                f"{model_name}: {str(exc)}"
            )

    raise RuntimeError(
        "Gemini document generation failed. "
        + " | ".join(errors)
    )
