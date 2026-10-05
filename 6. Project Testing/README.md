# 6. Project Testing – LegalEase

## 1. Introduction

Testing is an important phase of the LegalEase project. The purpose of testing is to verify that the application works correctly, generates legal document drafts based on user inputs, provides an editable preview, and supports document export.

The application is tested for functionality, input validation, Gemini AI integration, API functionality, user interface, and document export.

---

## 2. Testing Objectives

The main objectives of testing are:

- To verify that the LegalEase application starts correctly.
- To verify that users can enter all required details.
- To verify that the selected document type is processed correctly.
- To verify that Gemini AI generates a document draft.
- To verify that the generated document can be edited.
- To verify that the term table displays the entered information.
- To verify TXT document export.
- To verify DOCX document export.
- To verify PDF document export.
- To verify the health-check API.
- To verify proper error handling.
- To ensure that the Gemini API key is not exposed in the source code.

---

## 3. Testing Environment

### Hardware

- Intel Core i5 / AMD Ryzen 5 or equivalent
- Minimum 8 GB RAM
- Minimum 256 GB storage
- Stable Internet connection

### Software

- Windows / macOS / Linux
- Python 3.8 or above
- Visual Studio Code or any suitable IDE
- Git and GitHub
- Google Gemini API
- FastAPI
- Web browser

---

## 4. Functional Test Cases

| Test Case ID | Test Case | Input / Action | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Application startup | Run the FastAPI application | Application starts successfully | Pass |
| TC02 | Home page | Open the application in browser | LegalEase home page is displayed | Pass |
| TC03 | Document type selection | Select NDA | NDA is selected successfully | Pass |
| TC04 | User input | Enter party names, date, term and other details | Details are accepted | Pass |
| TC05 | Generate document | Click Generate Legal Document | AI-generated draft is displayed | Pass |
| TC06 | Editable preview | Edit generated document | User can modify the draft | Pass |
| TC07 | Term table | Generate a document | Entered terms are displayed in the table | Pass |
| TC08 | TXT export | Click Download TXT | TXT file is downloaded | Pass |
| TC09 | DOCX export | Click Download DOCX | DOCX file is downloaded | Pass |
| TC10 | PDF export | Click Download PDF | PDF file is downloaded | Pass |
| TC11 | Health check | Open `/health` | Application status is returned | Pass |
| TC12 | Missing required input | Submit form without required fields | Validation message is displayed | Pass |
| TC13 | Gemini API error | Use invalid/unavailable API key | Appropriate error message is displayed | Pass |
| TC14 | Security check | Inspect source code | API key is not hard-coded | Pass |

---

## 5. Document Type Testing

The following document types are tested:

### 5.1 Non-Disclosure Agreement (NDA)

Test whether the system generates an NDA draft using the details provided by the user.

### 5.2 Employment Agreement

Test whether the system generates an employment agreement using employer, employee, role, salary/consideration and other details.

### 5.3 Lease Agreement

Test whether the system generates a lease agreement using landlord, tenant, property, term and payment details.

### 5.4 Service Agreement

Test whether the system generates a service agreement using service provider, client, service description, payment and other terms.

---

## 6. API Testing

LegalEase provides API endpoints for application functionality.

### Health Check

Endpoint:

`GET /health`

Expected response:

```json
{
    "status": "running",
    "application": "LegalEase"
}
