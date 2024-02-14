#!/usr/bin/env python3



@app.before_request
def before_request():
    """ Before request handler """
    request.current_user = auth.current_user(request)
@app.route('/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a user """
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        else:
            return jsonify(request.current_user.to_dict())
    else:
        # Continue with the normal behavior
        # ...
