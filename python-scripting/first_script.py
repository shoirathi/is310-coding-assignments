
favorite_movies = [
    ("Toy Story", 1995),
    ("Cars", 2006),
    ("Django Unchained", 2012,),
    ("The Breakfast Club", 1985),
    ("Get Out", 2017),
    ("10 Things I Hate About You", 1999),
    ("The Wolf on Wall Street", 2013)
]
def check_movie_release(movie, release_year):
    if release_year < 2000:
        print(f"This movie was released before 2000")
    else:
        print(f"This movie was released after 2000")
        return movie
recent_movies = []
for movie, year in favorite_movies:
    result = check_movie_release(movie, year)
    if result is not None:
        recent_movies.append(result)

print("Recent movies:", recent_movies)