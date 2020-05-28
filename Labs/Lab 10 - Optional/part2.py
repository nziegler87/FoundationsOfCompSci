'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Optional Lab
    Description:
        Part 2 responses
'''

class Movie:
    ''' class: Movie
        Attributes: title, runtime, rating
        Methods: longer
    '''
    def __init__(self, title, runtime, rating):
        ''' Constructor: creates an instance of Movie
            Parameters:
                self -- the current object
                title -- move titel, a string
                runtime -- length of movie in minutes, an int
                rating -- movie rating, a string
        '''
        self.title = title
        self.runtime = runtime
        self.rating = rating

    def longer(self, other):
        ''' Method: longer
            Parameters:
                self -- the current object
                other -- another movie object
            Returns: true if self has a longer run-time than other, else False
        '''
        if self.runtime > other.runtime:
            return True
        else:
            return False

def add_longer(movie_list, movie):
    ''' Name: add_longer
        Parameters: a list of movie objects, a movie object
        Returns: an updated list
        Does: the given Movie object is appended to the list if it is longer
              than the Movie object currently in the last position of the list.
              Otherwise, the list is returned, unchanged.
    '''
    if not movie_lst:
        return movie
    if movie.runtime > movie_list[-1].runtime:
        movie_list.append(movie)
    return new_lst
