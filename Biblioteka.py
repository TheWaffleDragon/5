class Movie:
    def __init__(self, title, year, genre, times_seen):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_seen = times_seen
        

class TvShow(Movie):
    def __init__(self, epi, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.epi = epi
        self.season = season
        
