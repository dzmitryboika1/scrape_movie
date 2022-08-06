from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
movies_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies_list.reverse()
print(movies_list)

with open("movies.txt", "w") as movies:
    for movie in movies_list:
        movies.write(f"{movie}\n")
