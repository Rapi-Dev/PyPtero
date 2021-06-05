""" Majority of exceptions raised from the module """

class BaseError(Exception):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class ApiValidationError(BaseError):
    r""" Raised when your API token doesn't work with your domain """
    pass

