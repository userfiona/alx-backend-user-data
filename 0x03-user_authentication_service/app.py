#!/usr/bin/env python3
"""
Flask app
"""

from auth import Auth
from flask import Flask, abort, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/path_of_the_response', methods = ['GET'])
def ReturnJSON():
     """
    Index route that returns a json paylod
    """
    return jsonify({"message": "Bienvenue"})

# Make a register session for registration
@app.route("/users", methods=["POST"])
def users():
    """ New user signup endpoint
        Form fields:
            - email
            - password
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

        
# /login display login form 
@app.route("/sessions", methods=["POST"])
def login():
    """ Login endpoint
        Form fields:
            - email
            - password
        Return:
            - user email and login message JSON represented
            - 401 if credential are invalid
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response

 # Make function for logout session
@app.route("/sessions", methods=["DELETE"])
def logout():
    """ Logout endpoint
        Return:
            - redirect to home page
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect(url_for("home"))

@app.route("/profile")
def profile() -> str:
    """ User profile endpoint
        Return:
            - user email JSON represented
            - 403 if session_id is not linked to any user
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}i)



@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> str:
    """ Reset password token endpoint
        Form fields:
            - email
        Return:
            - email and reset token JSON represented
            - 403 if email is not associated with any user
    """
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token})


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """ Password update endpoint
        Form fields:
            - email
            - reset_token
            - new_password
        Return:
            - user email and password update message JSON represented
            - 403 if reset token is not provided or not linked to any user
    """
    email = request.form.get("email")
    new_password = request.form.get("new_password")
    reset_token = request.form.get("reset_token")

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
