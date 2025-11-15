# Data Extraction Service API (Django REST)

This project implements a backend service for managing data extraction jobs using **Django** and **Django REST Framework (DRF)**.  
It includes endpoints for creating extraction jobs, checking status, retrieving results with pagination, cancelling jobs, removing jobs, and viewing job statistics.  
Swagger/OpenAPI documentation is also provided.

---

## 🚀 Features

- Health check endpoint  
- Start a new extraction job  
- Check job status  
- Fetch job results (supports pagination)  
- Cancel extraction jobs  
- Remove extraction jobs  
- List all jobs (paginated)  
- Job statistics by status  
- Interactive API documentation (Swagger / OpenAPI)

---

## 🛠️ Tech Stack

- Python 3  
- Django 5  
- Django REST Framework  
- DRF Spectacular (Swagger UI)  
- SQLite (development)

---

## 📁 Project Structure
```
core/
│ settings.py
│ urls.py
extraction/
│ models.py
│ views.py
│ serializers.py
│ urls.py
manage.py
requirements.txt
.env.example
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/greentree_extraction_services.git
cd greentree_extraction_services
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv env
env\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Create .env file
```bash
cp .env.example .env
```
### 5️⃣ Run migrations
```bash
python manage.py migrate
```
### 6️⃣ Start the server
```bash
python manage.py runserver
```
## 📚 API Documentation (Swagger UI)
After starting the server, open the docs:

#### 👉 Swagger UI:
http://127.0.0.1:8000/api/docs/

#### 👉 Schema (OpenAPI JSON):
http://127.0.0.1:8000/api/schema/

---
## 🧪 API Endpoints Overview

Health Check
```bash
GET /api/v1/health
```
Start Extraction Job
```bash
POST /api/v1/scan/start
```
Job Status
```bash
GET /api/v1/scan/status/<job_id>
```
Extraction Results (Paginated)
```bash
GET /api/v1/scan/result/<job_id>?limit=20&offset=0
```
Cancel Extraction Job
```bash
POST /api/v1/scan/cancel/<job_id>
```
Remove Extraction Job
```bash
DELETE /api/v1/scan/remove/<job_id>
```
List All Jobs
```bash
GET /api/v1/jobs/jobs
```
Job Statistics
```bash
GET /api/v1/jobs/statistics
```
---
## 📌 Notes
SQLite is used for development as permitted.

Extraction logic is simulated; focus is on backend structure, endpoints, flows, and testing ability.

Swagger UI is auto-generated using DRF Spectacular.

---
## 🙋‍♀️ Author
Gargi Shringare

Backend Developer Intern — Assessment Project

