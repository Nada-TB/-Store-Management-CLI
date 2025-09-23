

class ChoiceInvalidError(Exception):
    """Raised when the user makes an invalid choice"""
    pass

class EmptyNameError(Exception):
    """Raised when the user enters an empty name"""
    pass
class IsNotAlphaError(Exception):
    pass
class EmptyItemError(Exception):
    pass
class ItemQuantityError(Exception):
    pass