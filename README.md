# Secure Notes API

A secure and robust RESTful API built using Python and FastAPI for creating, storing, retrieving, and managing personal notes with **JWT-based user authentication**, **role-based access control**, and **input validation**. 

>  Designed with a focus on **secure software development principles** to mitigate common vulnerabilities (OWASP Top 10) and ensure **confidentiality, integrity, and availability** of data.

---

## Overview

This API mimics the secure storage mechanisms used in corporate tools by applying strict user authentication and secure access to sensitive resources (notes). It serves as a demonstration of secure backend development with real-world applications in **risk management, compliance, and secure operations**.

---

## Key Features

- User registration and login
- Secure JWT authentication
- Create/read/update/delete (CRUD) personal notes
- Password hashing with `bcrypt`
- Role-based access (admin vs. user)
- Proper error handling
- Environment variable-based config management

---

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: SQLite (dev), PostgreSQL/MySQL (future)
- **Authentication**: JWT (PyJWT)
- **Security**: bcrypt, input validation, HTTP status handling
- **Tools**: Postman, Burp Suite (for testing), GitHub

---

## Security Measures

| Threat | Control/Implementation |
|-------|-------------------------|
| Broken Authentication | JWT + password hashing |
| Sensitive Data Exposure | Input validation + hashing |
| Injection Attacks | ORM/parameterized queries |
| Security Misconfig | `.env` for secrets, no secrets in code |
| Insufficient Logging | Planned log handler integration |
| Auth Bypass | Endpoint protection & token checks |
| Session Issues | JWT expiry & refresh flow (planned) |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /register | Register a new user |
| POST   | /login    | Authenticate user and return token |
| GET    | /notes    | Get all notes (user-specific) |
| POST   | /notes    | Create a new note |
| PUT    | /notes/{id} | Update a note |
| DELETE | /notes/{id} | Delete a note |

>  All routes except `/register` and `/login` require JWT authentication.

---

## Testing
Tested via Postman for CRUD and JWT handling.

- Security tested using Burp Suite:
- SQL Injection
- Auth bypass
- Broken access control
- Includes manual test cases for unauthorized access, tampered JWTs, and edge cases.


## Installation

```bash
git clone https://github.com/Harshvardhan1113/secure-notes-api.git
cd secure-notes-api
pip install -r requirements.txt
uvicorn main:app --reload


