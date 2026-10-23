"""Domain models: MediaItem and subclasses"""
VALID_STATUSES = ("to-do","in-progress","finished")
from mediashelf.exceptions import InvalidRatingError
from mediashelf.exceptions import InvalidStatusError

class MediaItem:
    """Base class for anything in the library."""

    def __init__(self, title, year, rating=None, status="to-do" ,genres=None):
        self.title = title
        self.year = year
        if rating is not None and (rating < 0 or rating > 5):
            raise InvalidRatingError("Rating must be between 0.0 and 5.0")
        self.rating = rating
        if status not in VALID_STATUSES:
            raise InvalidStatusError("Status must be one of: to-do, in-progress, finished!")
        self.status = status
        if genres is None:
            genres = []
        self.genres = {g.strip().lower() for g in genres}

class Book(MediaItem):
    """A book in the library"""
    def __init__(self, title, year, author, pages, rating=None, status="to-do",genres=None):
        super().__init__(title, year, rating, status,genres)
        self.pages = pages
        self.author = author

class Movie(MediaItem):
    """A movie In the library"""
    def __init__(self, title, year, director, runtime_minutes, rating=None, status="to-do",genres=None):
        super().__init__(title, year, rating, status,genres)
        self.director = director
        self.runtime_minutes = runtime_minutes

class Album(MediaItem):
    """An album in the library"""
    def __init__(self, title, year,  artist, tracks, rating=None, status="to-do",genres=None):
        super().__init__(title, year, rating, status, genres)
        self.artist = artist
        self.tracks = tracks
