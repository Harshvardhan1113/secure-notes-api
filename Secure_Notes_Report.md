# Secure Notes API – Project Report

## Abstract

The Secure Notes API is a Flask-based RESTful application that allows users to securely manage personal notes. It integrates user registration, JWT-based login, and full CRUD operations. The application also includes security testing to guard against common web vulnerabilities, aligning with OWASP recommendations.

---

## Objectives

- Build a secure and minimal REST API using Python and Flask
- Implement user authentication using JWT
- Enable note-taking with create, read, update, and delete operations
- Apply basic OWASP security testing using tools like Burp Suite and Postman

---

## Tech Stack

| Layer           | Technology        |
|----------------|-------------------|
| Language        | Python 3          |
| Framework       | Flask             |
| Auth System     | JWT (via `pyjwt`) |
| Database        | SQLite            |
| Tools Used      | Postman, Burp Suite, Git, GitHub |
| Deployment      | Localhost         |

---

## Features

- User registration with password hashing
- JWT-based login and token authentication
- Protected routes for all note operations
- Note ownership enforcement (user can only access their own notes)
- SQLite database for simplicity and portability

---

## Security Testing

Security tests were conducted using **Postman** and **Burp Suite** to simulate real-world attack vectors.

### Test Cases Performed:

| Test Type               | Description                                             | Result     |
|------------------------|---------------------------------------------------------|------------|
| SQL Injection (Login)  | Tried payloads like `' OR 1=1--`                        | ✅ Blocked |
| Token Tampering        | Modified/expired tokens used on protected routes        | ✅ Blocked |
| Missing Token Access   | Called protected endpoints without token                | ✅ Denied  |
| Replay Attack          | Re-used same JWT token after logout                     | ✅ Token Valid (as expected) |
| Header Manipulation    | Altered `Authorization` header formats                  | ✅ Blocked |
| Authorization Bypass   | Accessed another user's notes using ID tampering        | ✅ Denied  |

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

---

## API Overview

| Endpoint           | Method | Description            | Auth Required |
|--------------------|--------|------------------------|---------------|
| `/register`        | POST   | Register a new user    | ❌            |
| `/login`           | POST   | User login             | ❌            |
| `/notes`           | GET    | List all notes         | ✅            |
| `/notes`           | POST   | Create a new note      | ✅            |
| `/notes/<id>`      | GET    | Get a note by ID       | ✅            |
| `/notes/<id>`      | PUT    | Update a note          | ✅            |
| `/notes/<id>`      | DELETE | Delete a note          | ✅            |

---





## Conclusion

This project successfully demonstrates how to build a secure RESTful API using Flask and implement real-world protections against common vulnerabilities. It serves as a foundational backend system that can be extended to full-stack applications in the future.

---

