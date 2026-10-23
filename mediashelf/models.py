"""Domain models: MediaItem and subclasses"""
from mediashelf.exceptions import InvalidRatingError

class MediaItem:
    """Base class for anything in the library."""

    def __init__(self, title, year, rating=None, status="to-do"):
        self.title = title
        self.year = year
        if rating is not None and (rating < 0 or rating > 5):
            raise InvalidRatingError("Rating must be between 0.0 and 5.0")
        self.rating = rating
        self.status = status