*--------------Api for Frontend----------------*

Users

List all users (admin only)

GET /api/accounts/
-------------------------------------------------

Retrieve single user

GET    /api/accounts/<user_id>/
--------------------------------------------------

Delete single user (admin only)

DELETE /api/accounts/<user_id>/
---------------------------------------------------

Update user

PUT /api/accounts/update/<user_id>/
---------------------------------------------------

Register new user

POST /api/user_registration/

Sends verification email.
----------------------------------------------------
Login

POST /api/dj_rest_auth/login/


Returns tokens/session.
-----------------------------------------------------

Change password (logged-in user)

POST /api/dj_rest_auth/password/change/
------------------------------------------------------

Password Reset Flow

(a) Request password reset
POST /api/dj-rest-auth/password/reset/


Input:

{ "email": "user@example.com" }


Sends reset link to email:

http://localhost:3000/password-reset-confirm/{uid}/{token}


(b) Confirm password reset (React will call this API)
POST /api/dj_rest_auth/password/reset/confirm/


Input:

{
  "uid": "encoded-uidb64",
  "token": "reset-token",
  "new_password1": "newpassword",
  "new_password2": "newpassword"
}


Output (success):

{ "detail": "Password has been reset with the new password." }
---------------------------------------------------------------