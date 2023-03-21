import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["xtick.labelsize"] = 5
playerStats = pd.read_csv('cleaned-dataset/FIFA23PlayerStats.csv', index_col=0)
fig, axes = plt.subplots(2,2, figsize=(10,10), constrained_layout=True)

print(playerStats.info())
#sns.countplot(data=playerStats, x='Overall', ax=axes[0,0]).set(title='Countplot of Player Overall')
#sns.countplot(data=playerStats, x='Potential', ax=axes[0,1])

sns.histplot(data=playerStats, x='Body Type', ax=axes[0,0], kde=True)

sns.kdeplot(data=playerStats, x='HeightCM', ax=axes[1,0])
sns.kdeplot(data=playerStats, x='WeightKG', ax=axes[1,0])

sns.kdeplot(data=playerStats, x='WeightKG', hue='Grade', multiple='fill', ax=axes[0,1]).set(title='Distribution of Players wrt Weight')
sns.kdeplot(data=playerStats, x='HeightCM', hue='Grade', multiple='fill', ax=axes[1,1]).set(title='Distribution of Players wrt Height')


#plt.savefig('analysis/Distribution Analysis wrt Height, Weight and Body Type.png')
plt.show()
