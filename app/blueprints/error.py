from flask import Blueprint, jsonify
from flask import current_app

error_blueprint = Blueprint("error", __name__)


@error_blueprint.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    if not hasattr(error, "status_code"):
        status_code = 500
    else:
        status_code = error.status_code
    response = {
        "error": {"type": error.__class__.__name__, "message": message}
    }
    current_app.logger.debug(message)
    return jsonify(response), status_code
