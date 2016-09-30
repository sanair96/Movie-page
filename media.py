import webbrowser

class Movie():
    __name__="Movies" #name of class
    __module__="media" #name of module clas is present in
    """Class For an Awesome Movies page""" #Adds documentation
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showtrailer(self): #function to display trailer
        webbrowser.open(self.trailer_youtube_url)
