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

#%%
#Dodtkowe zadanie
'''
Napisz funkcje get_movies oraz get_series, które będą filtrować listę 
i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.
'''

def get_movies(watch_list):
    movies = []
    for i in watch_list:
        if type(i)==Movie:
            movies.append(i)
    return movies

movies_from_watch = get_movies(watch)    

def get_tv_shows(watch_list):
    tv_show = []
    for j in watch_list:
        if type(j)==TvShow:
            tv_show.append(j)
    return tv_show 

tv_show_from_watch = get_tv_shows(watch)    


 #%%   
'''
Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
'''

def search(watch_list,t):
    serched_title = []
    for i in watch_list:
        if i.title == t:
            serched_title.append(i)
    return serched_title
    
title_from_list = search(watch, 'tv_1')
#%%

'''
Napisz funkcję generate_views, która losowo wybiera element z biblioteki, 
a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
'''
import random as rnd

def generate_views(watch_list):
    x = rnd.randint(0, len(watch_list)-1)
    y = rnd.randint(1,100)
    watch_list[x].times_seen = y
    
    
generate_views(watch)





#%%
'''
Napisz funkcję, która uruchomi generate_views 10 razy.
'''
def gen_10(watch_list):
    for i in range(10):
        generate_views(watch_list)


gen_10(watch)




#%%
'''
Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych 
tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type, 
którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
'''

def sortby(watch_list):
    return watch_list.times_seen    

def top_titles(watch_list,n):
    s = watch_list.sort(reverse=True, key = sortby)
    for i in range(n):
        print (watch_list[i])
    

top_titles(watch, 2)

