class InvalidInputError(Exception):
    """Raised when input data is invalid."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NotFoundError(Exception):
    """Raised when a resource is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PermissionDeniedError(Exception):
    """Raised when permission to perform an action is denied."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CustomValidationError(Exception):
    """Raised when the serialization of an object fails."""
    def __init__(self, message, errors):
        self.message = message
        self.errors = errors
        super().__init__(self.message)