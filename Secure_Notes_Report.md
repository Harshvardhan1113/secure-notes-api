
# Secure Notes API – Project Report


---

## Project Overview

The **Secure Notes API** is a RESTful web service that provides users with secure access to create, store, and manage their personal notes. The application emphasizes secure development practices and has been tested for common web vulnerabilities to reflect real-world compliance, audit, and operational control environments.

---

## Key Functionalities

- **User Authentication** (Register/Login)
- **JWT-based token management**
- **Create, Read, Update, Delete** (CRUD) operations for personal notes
- **Security hardened endpoints** using validation, error handling

---

## Security Implementation & Testing

### Implemented Controls
- Passwords stored using `bcrypt` hashing
- Access control enforced at endpoint level via token scopes
- Exception handling to prevent sensitive data exposure
- Configs and secrets secured using `.env`

### Security Testing Tools
- **Postman** for API request validation and auth flow
- **Burp Suite** for vulnerability detection:
  - SQL Injection
  - Auth bypass attempts
  - Improper token usage
  - Session expiry testing

---

## Risk Mapping Table

| Risk Domain | Mitigation in API |
|-------------|-------------------|
| **Authentication Flaws** | JWT handling, token expiry |
| **Access Control Issues** | Endpoint-level role checks |
| **Data Exposure** | No sensitive data in logs or responses |
| **Injection Attacks** | Query validation + no raw queries |
| **Security Misconfigurations** | Proper use of environment variables |

---

## Iteration & Improvement Plan

- [ ] Add audit logging with timestamps and user IDs
- [ ] Integrate automated unit tests with coverage reports
- [ ] Implement admin/moderator role access
- [ ] Move to production-grade DB (PostgreSQL)
- [ ] Dockerize and deploy
- [ ] Enable Swagger + OAuth2 flows

---

## Outcome

- Demonstrated hands-on understanding of secure software development  
- Developed a system that can be extended into **secure corporate applications**
- Relevant to **risk control**, **reporting**, and **compliance** tracks.

---

