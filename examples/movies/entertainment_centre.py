import media
import fresh_tomatoes

toy_Story = media.Movie("Toy Story",
	"A story of a boy and his torys that come to lie",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Toy Story",
	"A story of a boy and his torys that come to lie",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")


movies = [toy_Story, avatar]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
