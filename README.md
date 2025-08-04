# Secure Notes API

A simple and secure Flask REST API for taking notes. It includes user registration, JWT-based login, and basic note management (CRUD). The project also includes basic security testing using Postman and Burp Suite.

---

## Features

- User registration and login
- JWT authentication for protected routes
- Create, read, update, delete personal notes
- SQLite database for easy local use
- Security tests for common vulnerabilities

---

## Security Testing (Basic)

- Used **Postman** to test APIs and token-based auth
- Used **Burp Suite** to try:
- SQL injection on login
- Auth bypass via invalid token
- Reused/expired tokens

---

## Setup Instructions

### Environment Setup

```bash
git clone https://github.com/yourusername/secure-notes-api.git
cd secure-notes-api
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

### Create `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/notes.db
```

### Run the App:

```bash
flask run
```



