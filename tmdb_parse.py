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
	adult = json_data['adult']*1 #convert ture to one, false to 0
	popularity = json_data['popularity']

	budget = json_data['budget']
	release_date = json_data['release_date']
	revenue = json_data['revenue']
	runtime = json_data['runtime']
	spoken_languages = ";".join([item['english_name'] for item in json_data['spoken_languages']])
	status = json_data['status']
	imdb_id = json_data['imdb_id']
	genres = ";".join([item['name'] for item in json_data['genres']])
	production_countries = ";".join([item['iso_3166_1'] for item in json_data['production_countries']])

	homepage = json_data['homepage']
	original_title = json_data['original_title']
	overview = json_data['overview']
	production_companies_id = ";".join([str(item['id']) for item in json_data['production_companies']])
	production_companies = ";".join([item['name'] for item in json_data['production_companies']])
	release_date = json_data['release_date']
	tagline = json_data['tagline']
	video = json_data['video']


	overview = overview.replace("\n", "").replace("\r", "") #replace the new line in genres


	# backdrop_path
	# poster_path


	# print(movie_id)
	# print(movie_title)

	df = pandas.concat([df,

	  pandas.DataFrame.from_records([{
		'movie_id': movie_id,
		'movie_title': movie_title,
		'vote_average': vote_average,
		'vote_count': vote_count,
		'adult': adult,
		'popularity': popularity,

		'budget': budget,
		'release_date': release_date,
		'revenue': revenue,
		'runtime': runtime,
		'spoken_languages': spoken_languages,		
		'status': status,
		'genres': genres,
		'imdb_id': imdb_id,
		'production_countries': production_countries,

		'homepage': homepage,
		'original_title': original_title,
		'overview': overview,
		'production_companies_id': production_companies_id,
		'production_companies': production_companies,
		'release_date': release_date,
		'tagline': tagline,
		'video': video

		}])
	  ])
 
# print(df)

df.to_csv("parsed_files/tmdb_dataset.csv",index=False)

print("done")

# what if we want adult to be 0 and non adult to be 1? think about it
# try to download other information in the csv file!
