def make_movie(movie_name, movie_studio, runtime= None):
    """Returns a dictionary stored with movie info"""
    movie_list = {'Movie name': movie_name , 'Studio' : movie_studio}
    if runtime:
        movie_list['runtime'] = runtime
    return movie_list
    #dictionary definition if statement to include runtime if passed

movie = make_movie('Thor: Ragnarok', 'Marvel', runtime = '3 hrs.')
movie1 = make_movie('Men in Black', 'New Line Cinema')

print(movie)
print(movie1)

#function call in definition of movie and print movie