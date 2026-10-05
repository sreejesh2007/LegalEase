import os
from google import genai


GEMINI_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
]


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. "
            "Please add your Gemini API key as an environment variable."
        )

    return genai.Client(api_key=api_key)


def generate_document(prompt):
    client = get_client()
    errors = []

    for model_name in GEMINI_MODELS:
        try:
            print(f"Trying Gemini model: {model_name}")

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            if response.text:
                print(f"Success with model: {model_name}")
                return response.text

        except Exception as error:
            print(f"Model {model_name} failed: {error}")
            errors.append(f"{model_name}: {error}")

    raise RuntimeError(
        "Gemini could not generate the document.\n\n"
        + "\n".join(errors)
    )


def build_legal_document(document_type, details):
    prompt = f"""
You are LegalEase, an AI-assisted legal document drafting system.

Create a professional GENERAL-PURPOSE LEGAL DOCUMENT DRAFT.

Document Type:
{document_type}

User-provided information:
{details}

Requirements:

1. Create a clear professional document.
2. Use appropriate headings.
3. Include the parties involved.
4. Include effective date where provided.
5. Include duration where relevant.
6. Include responsibilities and obligations.
7. Include payment terms where relevant.
8. Include confidentiality provisions where relevant.
9. Include termination provisions where relevant.
10. Include dispute-related wording where appropriate.
11. Include signature sections.
12. Do not invent personal information.
13. Do not claim that the document is legally valid in every jurisdiction.
14. Do not provide illegal or harmful instructions.
15. Clearly label the output as a legal document draft.
16. Use simple but professional legal language.

At the beginning include:

LEGAL DOCUMENT DRAFT
Prepared by LegalEase

At the end include:

DISCLAIMER:
This document is an AI-generated general-purpose draft and should be reviewed by a qualified legal professional before use.

Return only the document.
"""

    return generate_document(prompt)
