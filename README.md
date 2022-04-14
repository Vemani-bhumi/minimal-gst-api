# minimal-gst-api

This is a minimal gst api made using FastAPI.
Features:
1. Access and create users.
2. Access and create tax dues for each user.
3. After creation of a tax due it's status can only be modified if the user is authenticated/loggedin.

The schemas and models were created for users and tax dues. Passwords in users table are encrypted using the passlib library.
Authentication for patch request is done by creating jwt access tokens.
