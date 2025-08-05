# Screenshots & Functionality

## - Register a New User
#### Users can register by providing a unique username and secure password. Passwords are hashed using bcrypt before being stored in the database to ensure security.
---

## - Login to Get JWT Token
#### Upon successful login, a JWT access token is issued. This token is required for all authenticated requests. The token includes:
1. User identity
2. Expiry timestamp
3. Integrity via a secret key
---

## - Create a Note
#### A logged-in user can create personal notes using the /notes endpoint. The request body includes:
1. title
2. content
These notes are stored securely and linked to the authenticated user.
---

## Delete a Note

#### Users can delete their own notes using the note's unique ID. Proper checks ensure:
1. Only the owner can delete their notes
2. Unauthorized deletion attempts are blocked
---

