import media
import fresh_tomatoes

#Lines below create instances of the movies

kaththi = media.Movie("Kaththi","Story of a toy that is alive",
                       "https://upload.wikimedia.org/wikipedia/en/9/90/Kaththi_poster.jpg",
                       "https://www.youtube.com/watch?v=y7lFjlQHTv8")

the_dark_knight = media.Movie("The Dark Knight","Welcome to a World without Rules",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

inception = media.Movie("Inception","A Place where you never know if its a dream or not",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

interstellar = media.Movie("Interstellar","A Science fiction Time travelling, Mind twisting story",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

movies = [kaththi,the_dark_knight,inception,interstellar]

#Following code creates the HTML Page.

fresh_tomatoes.open_movies_page(movies)
