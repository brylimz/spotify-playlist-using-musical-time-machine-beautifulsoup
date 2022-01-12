from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
link_to_copy = "https://www.billboard.com/charts/year-end/" + date +"/hot-100-songs"
print(link_to_copy)
response = requests.get("https://www.billboard.com/charts/year-end/" + date +"/hot-100-songs")

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.find_all("h3", id="title-of-a-story")

song_names = [song.getText() for song in song_names_spans if len(song) != 100]

converted_song_names = []
for song in song_names:
    converted_song_names.append(song.strip())
new_list = converted_song_names[0:100]
df = pd.DataFrame(new_list, columns=["songs"])
new_df = df["NewCol1"] = "Number"

# new_file = df.to_csv("hoho.csv")