import urllib.request
import json
import os
import time


if not os.path.exists("json_files"):
	os.mkdir("json_files")

f = open("api_key","r")
api_key = f.read()
f.close()



response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/latest?api_key="+api_key)
# print(response.read())


json_response = json.load(response)

movie_max = int(json_response['id'])
movie_min = movie_max - 10

# print(movie_max)

for movie_id in range(movie_min, movie_max):
    print(movie_id)
    response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key="+api_key)
    json_response = json.load(response)

    f = open("json_files/tmdb_" + str(movie_id) + ".json", "w")
    f.write(json.dumps(json_response)) #remenber there is s after dump!
    time.sleep(30)

# watch the recording again! and what is the homework??? write some programs before the lecture, write tmdb_parse!