# 8. Project Demonstration – LegalEase

## 1. Project Introduction

LegalEase is an AI-powered legal document generator that uses Generative AI to create customizable legal document drafts based on user-provided information.

The application provides an easy interface for entering document details, generating a document, editing the generated content, and exporting the document in different formats.

---

## 2. Demonstration Objective

The objective of this demonstration is to show the complete working flow of the LegalEase application.

The demonstration covers:

- Selecting a legal document type
- Entering required information
- Generating a document using Gemini AI
- Viewing the generated document
- Editing the generated document
- Viewing the automatic term table
- Exporting the document
- Checking the application health status

---

## 3. Application Workflow

```text
User
  ↓
LegalEase Web Interface
  ↓
Enter Document Details
  ↓
FastAPI Backend
  ↓
Gemini AI
  ↓
Generate Legal Document Draft
  ↓
Editable Preview
  ↓
Automatic Term Table
  ↓
Export as TXT / DOCX / PDF
