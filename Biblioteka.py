class Movie:
    def __init__(self, title, year, genre, times_seen):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_seen = times_seen
    def play(self, times_seen):
        self.times_seen+=1
    def __repr__(self):
        return f"{self.title}({self.year})"
        

class TvShow(Movie):
    def __init__(self, epi, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.epi = epi
        self.season = season
    def play(self, times_seen):
        self.times_seen+=1
    def __repr__(self):
        return f"{self.title} S{self.season}E{self.epi}"
 
        
 
watch=[]

movie_1 = Movie(title="film_1", year="1990", genre="comedy", times_seen="5")
movie_2 = Movie(title="film_2", year="2033", genre="comedy", times_seen="1")

tv_1 = TvShow(epi='6', season='5', title='tv_1', year = '1956', genre='scifi', times_seen='3')
tv_2 = TvShow(epi='1', season='7', title='tv_2', year = '2006', genre='scifi', times_seen='0')

watch.append(movie_1)
watch.append(movie_2)
watch.append(tv_1)
watch.append(tv_2)


print(watch[0])
print(watch[2])
