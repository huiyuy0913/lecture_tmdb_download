import json
import pandas
import glob
import os

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")


df = pandas.DataFrame()

json_file_name = "json_files/tmdb_1032400.json"

f = open(json_file_name,"r")
json_data = json.load(f)
f.close()


movie_id = json_data['id']
movie_title = json_data['title']

print(movie_id)
print(movie_title)

df = pandas.concat([df,

  pandas.DataFrame.from_records([{
	'movie_id': movie_id,
	'movie_title': movie_title
	}])
  ])

# print(df)

df.to_csv("parsed_files/tmdb_dataset.csv",index=False)
