import requests
import os
import json
import time


if not os.path.exists("json_files_version2"):
    os.mkdir("json_files_version2")



f = open("api_key","r")
api_key = f.read()
f.close()


response = requests.get("https://api.themoviedb.org/3/movie/latest?api_key="+api_key)
# print(response.text)
json_response = json.loads(response.text)


movie_max = int(json_response['id'])
movie_min = movie_max - 10

# print(movie_max)

for movie_id in range(movie_min, movie_max):
	print(movie_id)
	response = requests.get("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key="+api_key)
	json_response = json.loads(response.text)

	f = open("json_files_version2/tmdb_" + str(movie_id) + ".json", "w")
	f.write(json.dumps(json_response))
	time.sleep(30)





