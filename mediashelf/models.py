"""Domain models: MediaItem and subclasses"""

class MediaItem:
    """Base class for anything in the library."""

    def __init__(self, title, year):
        self.title = title
        self.year = year