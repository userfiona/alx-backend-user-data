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
# session and also connect to Mysql to code for access
# login and for completing our login
# session and making some flashing massage for error
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in
        request.form and 'password' in request.form
            and 'email' in request.form:

       password = request.form['password']
        email = request.form['email']

        
# /login display login form 
@app.route('/login', methods = ['GET', 'POST'])  
  
# login function verify username and password 
def login():      
   error = None

   email = request.form.get("email")
   password = request.form.get("password")
     
   if request.method == 'POST': 
      if request.form['username'] != 'admin' or \ 
         request.form['password'] != 'admin': 
         error = 'Invalid username or password. Please try again !'
      else: 
  
         # flashes on successful login 
         flash('You were successfully logged in')  
         return redirect(url_for('index')) 
   return render_template('login.html', error = error) 

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
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
 @app.route('/profile', methods=['GET'])
def profile():
    """
    Finds user if existing in session or abort
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
