from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

#1 DOWNLOAD ----------------------
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)             # Open connection to server
raw_data = conn.read()          # Read data
page_content = raw_data.decode("utf8")   # Decode data

#2 --------------------------
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("section", "section chart-grid")
print(ul.prettify())
li_list = ul.find_all("li")

# #3 ---------------------------
# songs_list = []

# for li in li_list:
#     h3 = li.h3
#     h4 = li.h4
#     song_name = h3.string
#     artist = h4.string
#     # print(song_name)
#     # print(artist)
#     songs = OrderedDict({
#         "names": song_name,
#         "artists": artist,
#     })
#     songs_list.append(songs)
# # print(songs_list)
# # for st in songs_list:
# #     print(st["names"])
# #     print(st["artists"])


# #4 -----------------------------
# # pyexcel.save_as(records=songs_list,dest_file_name="Itunes_songs.xlsx")

# #5 SEARCH AND DOWNLOAD -----------------------
# options = {
#     "default_search": "ytsearch",
#     "max_downloads": len(songs_list),
#     "format": "bestaudio/audio",
# }
# dl=YoutubeDL(options)
# for st in songs_list:
#     search_keys = st["names"] + " " + st["artists"]
#     dl.download([search_keys])
