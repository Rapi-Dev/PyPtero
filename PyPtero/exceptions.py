""" Majority of exceptions raised from the module """

class BaseError(Exception):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class APIValidationError(BaseError):
    r""" Raised when your API token doesn't work with your domain """
    pass

class MissingAPIKey(BaseError):
    r""" Raised when either your API token is missing for a certain client """
    pass

class NotFound(BaseError):
    r""" Raised when a recourse cannot be found e.g. a user """
    pass