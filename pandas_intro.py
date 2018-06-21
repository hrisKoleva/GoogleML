# import pandas as pd
# import tensorflow as tf
# import numpy as np

# city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
# population = pd.Series([852469, 1015785, 485199])

# pd.DataFrame({ 'City name': city_names, 'Population': population })

# # print(city_names)

# # california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
# # california_housing_dataframe.describe()

# # california_housing_dataframe.head()
# # # california_housing_dataframe.hist()

# cities = pd.DataFrame({'City name': city_names, 'Population': population})
# # print(cities['City name'])
# # cities['City name']

# # print(cities['City name'][1])
# # cities['City name'][1]

# # print(cities[0:2])
# # cities[0:2]


# # print(np.log(population))
# print(population.apply(lambda val: val > 1000000))

# cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
# cities['Population density'] = cities['Population'] / cities['Area square miles']
# cities

# print(city_names)


import pandas as pd
import numpy as np

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])

# cities['Is named after a saint'] = city_names.apply(lambda val: 'San' in val)
# cities['Area more than 50'] = cities['Area square miles'].apply(lambda val: val > 50)

cities["New Column"] = city_names.apply(lambda name: name.startswith('San')) & (cities['Area square miles'] > 50)
#  city_names.apply(lambda val: 'San' in val)  & cities['Area square miles'].apply(lambda val: val > 50)

cities = cities.reindex(np.random.permutation(cities.index))
print(cities)