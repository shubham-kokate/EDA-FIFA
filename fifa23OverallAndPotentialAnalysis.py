import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["xtick.labelsize"] = 5
playerStats = pd.read_csv('cleaned-dataset/FIFA23PlayerStats.csv', index_col=0)
fig, axes = plt.subplots(2,2, figsize=(10,10), constrained_layout=True)

print(playerStats.info())
#sns.countplot(data=playerStats, x='Overall', ax=axes[0,0]).set(title='Countplot of Player Overall')
#sns.countplot(data=playerStats, x='Potential', ax=axes[0,1])

sns.scatterplot(data=playerStats, x='Potential', y='Overall', hue='Grade', ax=axes[0,0]).set(title='Overall vs Potential Scatterplot')

sns.kdeplot(data=playerStats, x='Overall', ax=axes[1,0]).set(title='Distribution of Player wrt Overall and Potential', xlabel='Overall and Potential')
sns.kdeplot(data=playerStats, x='Potential', ax=axes[1,0])

sns.kdeplot(data=playerStats, x='Overall', hue='Grade', multiple='stack', ax=axes[1,1]).set(title='Distribution of Players wrt Overall and Grade')
sns.kdeplot(data=playerStats, x='Potential', hue='Grade', multiple='stack', ax=axes[0,1]).set(title='Distribution of Players wrt Potential and Grade')

plt.savefig('analysis/Distribution Analysis wrt Overall, Potential and Grade.png')
#plt.show()
