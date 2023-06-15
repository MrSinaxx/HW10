import requests

base_url = "https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api"

def get_movie_list():
    url = f"{base_url}/movies"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()
        for movie in movies:
            title = movie.get('Title', 'N/A')
            year = movie.get('Year', 'N/A')
            if title == 'N/A' or year == 'N/A':
                print("Skipping movie due to missing key.")
                continue
            print(f"Title: {title}")
            print(f"Year: {year}")
            print("")

def add_movie():
    title = input("Enter the title of the movie: ")
    year = input("Enter the year of the movie: ")


    url = f"{base_url}/movies"
    data = {
        "Title": title,
        "Year": year
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Movie successfully added to the system.")
    else:
        print("Failed to add the movie to the system.")


get_movie_list()
add_movie()
