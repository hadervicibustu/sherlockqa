# Register User

Register a new user in the database with the provided email address.

## Arguments

- `$ARGUMENTS` - The email address for the new user (required)

## Instructions

Make a POST request to the `/api/auth/register` endpoint to register a new user.

1. First, validate that an email argument was provided. If `$ARGUMENTS` is empty, inform the user they need to provide an email:
   ```
   Usage: /register-user <email>
   Example: /register-user user@example.com
   ```

2. Check if the backend server is running by making a simple request

3. Call the register endpoint using curl:
   ```
   curl -X POST http://localhost:5000/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email": "<email>"}'
   ```

4. Report the results to the user, including:
   - Success message with user details if registration succeeded
   - Error message if registration failed (e.g., user already exists, invalid email)

If the server is not running, inform the user they need to start the backend server first with:
```
cd backend && python run.py
```

The endpoint will:
- Validate the email format
- Check if user already exists
- Create a new user record in PostgreSQL
- Return the created user details
