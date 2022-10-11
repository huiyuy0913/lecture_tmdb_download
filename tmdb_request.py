import urllib.request  # you can also use requests to do it
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

# movie_max = int(json_response['id'])
# movie_min = movie_max - 200

movie_max = 1022400
movie_min = 1022300

# print(movie_max)

for movie_id in range(movie_min, movie_max):
    file_name = "json_files/tmdb_" + str(movie_id)

    if os.path.exists(file_name + ".json"):
        print("file exists", movie_id)
    else:
        try:
            print("downloading:",movie_id)
            response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key="+api_key)
            json_response = json.load(response)

            f = open(file_name + ".tmp", "w")
            f.write(json.dumps(json_response)) #remember there is s after dump!
            f.close()


            time.sleep(1)
            os.rename(file_name + ".tmp", file_name + ".json")
        except Exception as e:
            print(e)


        print("waiting 15 seconds")
        time.sleep(15)

# watch the recording again! and what is the homework??? write some programs before the lecture, write tmdb_parse!