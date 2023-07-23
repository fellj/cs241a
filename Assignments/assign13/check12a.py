#use Pandas to load this dataset and then to filter it to find the median age

import pandas
census_file ="L:\Lisa\School\Spring21\CS241\Code\Python\week12\census.csv" 
census_data = pandas.read_csv(census_file)

print(census_data.age)

median_age = census_data.age.median()
print("The Median Age in the census file is " + str(round(median_age)))