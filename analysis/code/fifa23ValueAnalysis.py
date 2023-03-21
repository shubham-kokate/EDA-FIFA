import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["xtick.labelsize"] = 5
playerStats = pd.read_csv('cleaned-dataset/FIFA23PlayerStats.csv', index_col=0)
fig, axes = plt.subplots(2,2, figsize=(10,10), constrained_layout=True)

meanValueGrade4 = playerStats[(playerStats['Value']!=0) & (playerStats['Grade']==4)].mean(numeric_only=True)['Value']
meanValueGrade3 = playerStats[(playerStats['Value']!=0) & (playerStats['Grade']==3)].mean(numeric_only=True)['Value']
meanValueGrade2 = playerStats[(playerStats['Value']!=0) & (playerStats['Grade']==2)].mean(numeric_only=True)['Value']
meanValueGrade1 = playerStats[(playerStats['Value']!=0) & (playerStats['Grade']==1)].mean(numeric_only=True)['Value']

for i in range(len(playerStats['Value'])):
    if playerStats.iloc[i, 6]==0:
        if playerStats.iloc[i, 12]==4:
            playerStats.iloc[i, 6] = meanValueGrade4
        elif playerStats.iloc[i, 12]==3:
            playerStats.iloc[i, 6] = meanValueGrade3
        elif playerStats.iloc[i, 12]==2:
            playerStats.iloc[i, 6] = meanValueGrade2
        elif playerStats.iloc[i, 12]==1:
            playerStats.iloc[i, 6] = meanValueGrade1

#Binning by Player Value
playerStats.loc[playerStats['Value'].between(0,0.3, 'both'), 'Value Grade'] = 'Very Low'
playerStats.loc[playerStats['Value'].between(0.3,0.6, 'right'), 'Value Grade'] = 'Low'
playerStats.loc[playerStats['Value'].between(0.6,5, 'right'), 'Value Grade'] = 'Medium'
playerStats.loc[playerStats['Value'].between(5,50, 'right'), 'Value Grade'] = 'High'
playerStats.loc[playerStats['Value'].between(50,playerStats['Value'].max(), 'right'), 'Value Grade'] = 'Very High'

playerStatsOver75 = playerStats[playerStats['Overall']>75]
print(playerStatsOver75.info())

sns.scatterplot(data=playerStatsOver75, x='Overall', y='Value', hue='Value Grade', ax=axes[0,0])

sns.scatterplot(data=playerStats, x='Overall', y='Value', hue='Value Grade', ax=axes[0,1])
sns.scatterplot(data=playerStats, x='Potential', y='Value', hue='Value Grade', ax=axes[1,1])


plt.show()
