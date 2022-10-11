
import pandas
tmdb_dataset = pandas.read_csv('/Users/heidi/Desktop/ECON860/lecture_tmdb_download/parsed_files/tmdb_dataset.csv', lineterminator='\n')
print(tmdb_dataset["adult"])
# tmdb_dataset['adult'][tmdb_dataset['adult'] == 0] = 1
# tmdb_dataset['adult'][tmdb_dataset['adult'] == 1] = 0

# # method2
size_mapping = {0: 1, 1: 0}
tmdb_dataset['adult'] = tmdb_dataset['adult'].map(size_mapping)
print(tmdb_dataset["adult"])

tmdb_dataset.to_csv("parsed_files/tmdb_dataset.csv",index=False)

# tmdb_dataset.replace(1,0,inplace = True)
# tmdb_dataset.replace(0,1,inplace = True)
# print (tmdb_dataset["adult"])
