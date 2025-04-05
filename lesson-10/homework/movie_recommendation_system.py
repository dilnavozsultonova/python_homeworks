import requests
import random

api_key="4276f5dfd9ac7d01409c822d669de90d"
base_url=f"https://api.themoviedb.org/3/"

def get_genres():
    url = f'{base_url}genre/movie/list?api_key={api_key}&language=en-US'
    response=requests.get(url)

    if response.status_code==200:
        genres=response.json()['genres']
        genre_dict={genre['id']: genre ['name'] for genre in genres}
        return genre_dict
    else:
        print("Error fetching genres:{response.status_code}")
        return None
    
def get_movie_by_genre(genre_id):
    url = f'{base_url}discover/movie?api_key={api_key}&with_genres={genre_id}&language=en-US'
    response=requests.get(url)

    if response.status_code==200:
        movies=response.json()['results']
        return movies
    else:
        print("Error fetching genres {response.status_code}")
        return None
    
def recommend_movie():
   
    genres = get_genres()
    
    if not genres:
        return

    print("Available genres:")
    for genre_id, genre_name in genres.items():
        print(f"{genre_id}. {genre_name}")

    genre_id = input("Enter the genre ID you'd like to explore: ")

    
    if not genre_id.isdigit() or int(genre_id) not in genres:
        print("Invalid genre ID. Please try again.")
        return

    genre_id = int(genre_id)


    movies = get_movie_by_genre(genre_id)

    if not movies:
        return

   
    random_movie = random.choice(movies)
    movie_title = random_movie['title']
    movie_overview = random_movie['overview']
    movie_release_date = random_movie['release_date']

    print(f"\nRecommended Movie: {movie_title}")
    print(f"Release Date: {movie_release_date}")
    print(f"Overview: {movie_overview}")


if __name__ == "__main__":
    recommend_movie()
    

