from flask import abort
from functools import wraps


def roles_required(*role_names):
    def wrapper(view_function):
        @wraps(view_function)
        def decorator(*args, **kwargs):

            # if not current_user.is_authenticated:
            #     return abort(401)
            #
            # if not current_user.has_roles(*role_names):
            #     return abort(401)

            return view_function(*args, **kwargs)

        return decorator

    return wrapper
