from flask import Blueprint, jsonify

error_blueprint = Blueprint("error", __name__)


@error_blueprint.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = 401
    response = {
        "error": {"type": error.__class__.__name__, "message": message}
    }
    return jsonify(response), status_code
