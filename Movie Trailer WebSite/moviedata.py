import myclass
import fresh_tomatoes

#creating instances of Movie class

cap_america = myclass.Movie("Captain America","http://static.rogerebert.com/uploads/movie/movie_poster/captain-america-civil-war-2016/large_large_5N20rQURev5CNDcMjHVUZhpoCNC.jpg","https://www.youtube.com/watch?v=uVdV-lxRPFo")


finding_dory = myclass.Movie("Finding Dory","http://alisakwitney.com/wp-content/uploads/2016/06/FindingDory_Wide.jpg","https://www.youtube.com/watch?v=MKJA-VLpiCo")

zootopia = myclass.Movie("Zootopia","http://assets.nnm-club.ws/forum/image.php?link=http://i5.imageban.ru/out/2016/06/07/d925f4f5e394c1c11316cf2909f1c390.jpg","https://www.youtube.com/watch?v=jWM0ct-OLsM")

jungle_book = myclass.Movie("The Zungle Book","https://lumiere-a.akamaihd.net/v1/images/movie_poster_junglebook2016_27cac229.jpeg?region=0%2C0%2C300%2C450","https://www.youtube.com/watch?v=5mkm22yO-bs")

dead_pool = myclass.Movie("Deadpool","https://www.sideshowtoy.com/assets/products/902628-deadpool/lg/marvel-deadpool-sixth-scale-hot-toys-902628-17.jpg","https://www.youtube.com/watch?v=FyKWUTwSYAs")

secret_life = myclass.Movie("The Secret Life of Pets","https://i.ytimg.com/vi/k8T1EGEGuX0/maxresdefault.jpg","https://www.youtube.com/watch?v=UZJVc_JTI_w")

#harry.show_trailer()
#storing instances of Movie class in an array named 'movies'
movies =[cap_america,finding_dory,zootopia,jungle_book,dead_pool,secret_life]
fresh_tomatoes.open_movies_page(movies)
