# import matplotlib.pyplot as plt
# 
# ... other things here ...
# 
# 
# data.mean_temp.hist()
# 
# # if nothing pops up, you can then do:
# plt.show()


import pandas

import matplotlib.pyplot as plt

data = pandas.read_csv("L:\Lisa\School\Spring21\CS241\Code\Python\week12\weather_year.csv")

#print(data)

#print(len(data))

#print(data.columns)

#print(data[["EDT", "Mean TemperatureF"]])

#print(data.EDT)

print(data.EDT.head(10))


