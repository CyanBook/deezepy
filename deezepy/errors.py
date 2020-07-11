class DeezerError(Exception):
    """
    Subclass of python ``Exception`` class, it can handle every Deezepy error
    Every specific error is a subclass of this class
    """


class QuotaExceeded(DeezerError):
    """Raised when too many requests are being made"""

    def __init__(self):
        super().__init__("Too many requests")


class ItemsLimitExceeded(DeezerError):
    """Raised when the limit is greater than the maximum allowed"""

    def __init__(self):
        super().__init__("The limit is greater than the maximum allowed")


class Permission(DeezerError):
    """Raised when you don't have the permission for the required action"""

    def __init__(self):
        super().__init__("You don't have the permission to complete this action")


class TokenInvalid(DeezerError):
    """Raised when the token is invalid"""

    def __init__(self):
        super().__init__("The token is invalid")


class Parameter(DeezerError):
    """Raised when a parameter is wrong"""

    def __init__(self):
        super().__init__("A parameter is wrong")


class ParameterMissing(DeezerError):
    """Raised when a required parameter is missing"""

    def __init__(self):
        super().__init__("A required parameter is missing")


class QueryInvalid(DeezerError):
    """Raised when the query is invalid"""

    def __init__(self):
        super().__init__("The query is invalid")


class ServiceBusy(DeezerError):
    """Raised when the API can't handle the load"""

    def __init__(self):
        super().__init__("The service is busy")


class DataNotFound(DeezerError):
    """Raised when the data requested isn't found"""

    def __init__(self):
        super().__init__("The data requested can't be found")


class IndividualAccountNotAllowed(DeezerError):
    """Raised when an individual account isn't allowed"""

    def __init__(self):
        super().__init__("An individual account isn't allowed")
