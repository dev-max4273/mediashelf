"""Domain models: MediaItem and subclasses"""

class MediaItem:
    """Base class for anything in the library."""

    def __init__(self, title, year, rating=None, status="to-do"):
        self.title = title
        self.year = year
        self.rating = rating
        self.status = status