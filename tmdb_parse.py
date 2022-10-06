import json
import pandas
import glob
import os

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")


df = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):

	# json_file_name = "json_files/tmdb_1032400.json"
	f = open(json_file_name,"r")
	json_data = json.load(f)
	f.close()


	movie_id = json_data['id']
	movie_title = json_data['title']
	vote_average = json_data['vote_average']
	vote_count = json_data['vote_count']

	# print(movie_id)
	# print(movie_title)

	df = pandas.concat([df,

	  pandas.DataFrame.from_records([{
		'movie_id': movie_id,
		'movie_title': movie_title,
		'vote_average': vote_average,
		'vote_count': vote_count
		}])
	  ])

# print(df)

df.to_csv("parsed_files/tmdb_dataset.csv",index=False)

print("done")