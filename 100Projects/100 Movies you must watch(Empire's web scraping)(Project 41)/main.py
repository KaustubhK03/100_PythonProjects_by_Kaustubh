import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
hundred_movies_html = response.text
soup = BeautifulSoup(hundred_movies_html, "html.parser")
movies_list = soup.find_all(name="h3", class_="title")
hundred_movies_lst = [movie_tag.get_text() for movie_tag in movies_list]
hundred_movies_lst.reverse()

with open(file="Movies to watch.txt", mode="w") as file:
    for movie in hundred_movies_lst:
        file.write(f"{movie}\n")