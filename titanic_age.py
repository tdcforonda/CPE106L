import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('titanic_1.csv', index_col='PassengerID')
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age(years)')
plt.ylabel('count')
plt.show()