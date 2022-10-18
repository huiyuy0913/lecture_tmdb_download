import pandas
import numpy

import matplotlib.pyplot as plt

dataset = pandas.read_csv("parsed_files/tmdb_dataset.csv", lineterminator='\n') 

print(dataset)

print(dataset.describe())
print("----------")


### check how many movies has vote average 0
# dataset['zero_score'] = (['vote_average'] == 0)*1

# print(dataset['zero_score'].sum())

### generate new column by a condition

# dataset['popular'] = (dataset['popularity'] > 30)*1

### count missing value and drop them
print(dataset.isna().sum())

dataset = dataset.dropna(subset=['release_date'])

print(dataset.isna().sum())


print(dataset)
print(dataset.describe())


# sub_dataset = dataset[(dataset['budget']>0) & (dataset['revenue']>0)]

# print(sub_dataset)
# print(sub_dataset.describe())


# revenue = sub_dataset['revenue']
# budget = sub_dataset['budget']
# vote_average = sub_dataset['vote_average']

# logrevenue = numpy.log(revenue)
# logbudget = numpy.log(budget)

# plt.scatter(logbudget, logrevenue, c=vote_average)
# plt.title("Budget and Revenue")
# plt.ylabel("Revenue")
# plt.xlabel("Budget")
# plt.colorbar()
# plt.savefig('figure.png')