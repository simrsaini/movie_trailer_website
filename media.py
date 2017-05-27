class Movie():
    #datastructure for movie titles
    MOVIE_TITLE= ["Toy Story", "Avatar", "Wall-E", "Beauty And ThE Beast", "Frozen", "Inside Out"]

    #datstructure for poster images source
    POSTER_IMAGE= ["https://cdn.europosters.eu/image/3d/15473.gif",
		   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
		   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", 
		   "http://dx35vtwkllhj9.cloudfront.net/disney/beauty-and-the-beast/images/regions/au/onesheet.jpg", 
		   "https://pop.inquirer.net/files/2017/04/57626-160613_1465794713056.jpeg", 
		   "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"]

    #datastructure for trailer links
    TRAILER_YOUTUBE= ["https://www.youtube.com/watch?v=KYz2wyBy3kc",
		      "https://youtu.be/cRdxXPV9GNQ", 
		      "https://youtu.be/ZisWjdjs-gM", 
		      "https://youtu.be/c38r-SAnTWM", 
		      "https://youtu.be/FLzfXQSPBOg", 
		      "https://youtu.be/seMwpP0yeu4"]

    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image = poster_image
        self.trailer_youtube_url = trailer_youtube

