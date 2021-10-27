import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('house_votes.csv')
plt.figure()

sns.countplot(x='sat_test', hue = 'party', data = df, palette = 'RdBu')
plt.xticks([0, 1], ['No', 'Yes'])
plt.legend(loc = 'best')
plt.show()