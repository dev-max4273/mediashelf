"""Domain models: MediaItem and subclasses"""
VALID_STATUSES = ("to-do","in-progress","finished")
from mediashelf.exceptions import InvalidRatingError
from mediashelf.exceptions import InvalidStatusError

class MediaItem:
    """Base class for anything in the library."""

    def __init__(self, title, year, rating=None, status="to-do"):
        self.title = title
        self.year = year
        if rating is not None and (rating < 0 or rating > 5):
            raise InvalidRatingError("Rating must be between 0.0 and 5.0")
        self.rating = rating
        if status not in VALID_STATUSES:
            raise InvalidStatusError("Status must be one of: to-do, in-progress, finished!")
        self.status = status