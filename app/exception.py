class InvalidToken(Exception):
    status_code = 401


class AuthRequired(Exception):
    status_code = 401


class InvalidAuthUser(Exception):
    status_code = 401


class StackError(Exception):
    status_code = 500
