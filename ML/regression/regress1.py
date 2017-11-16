import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col =0)
data.head()
data.shape

#visualize the relationship between features and response using scatterplots
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='TV', y='Sales', ax = axs[0], figsize = (16,8))

#plt.xlabel("TV")
#plt.ylabel("Sales")

#plt.show()
