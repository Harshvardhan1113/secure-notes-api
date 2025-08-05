# Secure Notes API

A security-focused notes-taking REST API built with **FastAPI**, demonstrating secure user authentication, token handling, and protected CRUD operations. Designed as a backend project to showcase principles of secure software development and API-level threat prevention.

---

## Tech Stack

- **Python 3.11**
- **FastAPI**
- **OAuth2 with Password (Bearer Token)**
- **JWT (JSON Web Tokens)**
- **Bcrypt** (for password hashing)
- **SQLite** (for lightweight data storage)

---

## Features

### User Authentication
- User **Registration** and **Login** with hashed passwords
- **JWT Token** generation and expiration handling
- Authentication via **OAuth2 password flow**

### Secure Notes Management
- **CRUD operations** for personal notes
- Routes are protected — only authenticated users can access their own notes

### Security Measures
- Passwords are stored securely with **bcrypt hashing**
- Token-based route protection with FastAPI’s dependency injection
- Prepared for **SQL Injection testing** and **auth bypass testing**
- All endpoints return appropriate **HTTP status codes**

---

## Installation & Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Harshvardhan1113/secure-notes-api.git
   cd secure-notes-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

4. Visit:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   for the auto-generated Swagger UI

---

## API Endpoints Overview

| Method | Endpoint        | Description              | Auth Required |
|--------|------------------|--------------------------|---------------|
| POST   | `/register`      | Create a new user        | ❌            |
| POST   | `/token`         | Login & get token        | ❌            |
| GET    | `/notes/`        | Get all notes            | ✅            |
| POST   | `/notes/`        | Create a note            | ✅            |
| GET    | `/notes/{id}`    | Get a specific note      | ✅            |
| PUT    | `/notes/{id}`    | Update a note            | ✅            |
| DELETE | `/notes/{id}`    | Delete a note            | ✅            |

---

## Security Testing (In Progress)

| Attack Type            | Tested With | Status                |
|------------------------|-------------|------------------------|
| SQL Injection          | Postman     | ✅ Blocked by ORM      |
| JWT Tampering          | Postman/Burp Suite | ✅ Invalid token rejected |
| Tokenless Access       | Postman     | ✅ Access denied       |
| Forced Browsing        | Burp Suite  | ✅ Access denied       |



**Screenshots and test results will be added soon**

---

## Relevance to Security & Risk Roles

This project demonstrates:
- Secure backend design principles
- API-level access control
- Threat simulation and mitigation
- Real-world auth workflows using OAuth2 + JWT

---

## Screenshots (To be added)

- Postman requests with and without token
- Burp Suite scans for endpoint vulnerabilities
- Token decoding and expiry handling

---

## Future Enhancements

- Role-based access (RBAC)
- Token revocation & blacklist
- Docker support
- CI/CD integration for testing
- Database migration support via Alembic

---
