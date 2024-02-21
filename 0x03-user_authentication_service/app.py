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

        
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in
    request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor
                (MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM user WHERE email = % s AND password = % s',
                  (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully !'
            return render_template('user.html',
                                   message=message)
        else:
            message = 'Please enter correct email / password !'
    return render_template('login.html',
                           message=message)

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
