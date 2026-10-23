""" Custom Exceptions for MediaShelf"""


class MediaShelfError(Exception):
    """Base class for all MediaShelf errors"""
    pass

class InvalidRatingError(MediaShelfError):
    """Raised when a rating is outside 0.0 to 5.0"""
    pass

class ItemNotFoundError(MediaShelfError):
    """Raised when no item exists with a given ID"""
    pass

class DuplicateItemError(MediaShelfError):
    """Raised when an item with the same type, title and year already exists"""
    pass

class InvalidStatusError(MediaShelfError):
    """Status isn't to-do, in-progress or finished"""
    pass

class StorageError(MediaShelfError):
    """A file can't be read or written, or the JSON is corrupted"""
    pass

class InvalidYearError(MediaShelfError):
    """Raised when a year is outside the allowed range"""