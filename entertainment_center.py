import media
import fresh_tomatoes

#multiple instance are created
TOY_STORY = media.Movie(media.Movie.MOVIE_TITLE[0], media.Movie.POSTER_IMAGE[0], media.Movie.TRAILER_YOUTUBE[0]) 
AVATAR = media.Movie(media.Movie.MOVIE_TITLE[1], media.Movie.POSTER_IMAGE[1], media.Movie.TRAILER_YOUTUBE[1])
WALLE = media.Movie(media.Movie.MOVIE_TITLE[2], media.Movie.POSTER_IMAGE[2], media.Movie.TRAILER_YOUTUBE[2])
BAB = media.Movie(media.Movie.MOVIE_TITLE[3], media.Movie.POSTER_IMAGE[3], media.Movie.TRAILER_YOUTUBE[3])
FROZEN = media.Movie(media.Movie.MOVIE_TITLE[4], media.Movie.POSTER_IMAGE[4], media.Movie.TRAILER_YOUTUBE[4])
IO = media.Movie(media.Movie.MOVIE_TITLE[5], media.Movie.POSTER_IMAGE[5], media.Movie.TRAILER_YOUTUBE[5])

#List of instances is created
MOVIES = [TOY_STORY, AVATAR, WALLE, BAB, FROZEN, IO]

#object is passed to open_movies_page method of fresh_tomatoes
fresh_tomatoes.open_movies_page(MOVIES)
