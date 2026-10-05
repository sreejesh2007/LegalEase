# 3. Project Design Phase

## System Architecture

```text
User
 |
 v
HTML/CSS Interface
 |
 v
FastAPI Application
 |
 +----------------------+
 |                      |
 v                      v
Input Validation    Gemini AI Service
 |                      |
 +----------+-----------+
            |
            v
     Generated Document
            |
            v
      Editable Preview
            |
            v
    Important Terms Table
            |
            v
 PDF / DOCX / TXT
