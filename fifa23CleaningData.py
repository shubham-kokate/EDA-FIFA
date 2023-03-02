import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt


fifa23df = pd.read_csv('FIFA23_official_data.csv')

#setting index starting from 1
i = range(1, len(fifa23df)+1)
fifa23df.index = i


#visualizing data
#print(fifa23df.isnull().sum())
#print(fifa23df.info())
#print(fifa23df['Club'].isnull().sum())


#Making a Player Physicals Dataset

#Dropping unecessary columns:
unecessary_cols = ['Loaned From', 'Best Overall Rating', 'Photo', 'Flag', 'Club', 'Club Logo', 'Wage', 'Special', 'International Reputation', 'Weak Foot', 'Skill Moves', 'Work Rate', 'Real Face', 'Joined', 'Contract Valid Until', 'Release Clause', 'Kit Number']
playerStats = fifa23df.drop(unecessary_cols, axis=1)\

#print(playerStats.info())

#Renaming Required Columns:
playerStats.rename(columns={
    'Height': 'HeightCM',
    'Weight': 'WeightKG'
}, inplace=True)


#checking null values:
#print(playerStats.isnull().sum())

#checking the unique values in two columns with nulls (Body Type, Position)
#print(playerStats['Body Type'].unique())
#print(playerStats['Position'].unique())

#Checking for NaN values in POSITIONS and replacing with RES
#print(playerStats[playerStats['Position'].isna()])
playerStats['Position'] = playerStats['Position'].fillna('<span class="pos pos29">RES')

#Checking for NaN values in Body Type and replacing with NORMAL
#print(playerStats[playerStats['Body Type'].isna()])
playerStats['Body Type'] = playerStats['Body Type'].fillna('Normal (170-185)')

#clearing position values to correct Positions According to the Game
old_positions = []
for position in playerStats['Position'].unique():
    old_positions.append(position)

#creating a new array of values to replace old ones
new_positions = []
for position in old_positions:
    new_positions.append(position.split(">")[1])

#replacing values
playerStats['Position'] = playerStats['Position'].replace(old_positions, new_positions)


#Correcting DataTypes and Values of Required Columns

#Removing €, M and K from Value so that it can be converted to float:
for i in range(len(playerStats['Value'])):
    playerStats.iloc[i, 6] = playerStats.iloc[i, 6].replace('€', '')
    playerStats.iloc[i, 6] = playerStats.iloc[i, 6].replace('M', '')
    playerStats.iloc[i, 6] = playerStats.iloc[i, 6].replace('K', '')

#Removing 'CM' from Height:
for i in range(len(playerStats['HeightCM'])):
    playerStats.iloc[i, 10] = playerStats.iloc[i, 10].replace('cm','')

#Removing 'KG' from Weight:
for i in range(len(playerStats['WeightKG'])):
    playerStats.iloc[i, 11] = playerStats.iloc[i, 11].replace('kg','')


playerStats = playerStats.convert_dtypes()

playerStats['HeightCM'] = playerStats['HeightCM'].astype(np.int64)
playerStats['WeightKG'] = playerStats['WeightKG'].astype(np.int64)

playerStats = playerStats.convert_dtypes()


#Binning Players according to Overall in 5 Star System
playerStats.loc[playerStats['Overall'].between(85,100, 'left'), 'Grade'] = '5'
playerStats.loc[playerStats['Overall'].between(75,85, 'left'), 'Grade'] = '4'
playerStats.loc[playerStats['Overall'].between(65,75, 'left'), 'Grade'] = '3'
playerStats.loc[playerStats['Overall'].between(55,65, 'left'), 'Grade'] = '2'
playerStats.loc[playerStats['Overall'].between(playerStats['Overall'].min(),55, 'left'), 'Grade'] = '1'

#print(playerStats['Grade'].value_counts().sort_index())
playerStats = playerStats.convert_dtypes()
print(playerStats.info())

playerStats.to_csv("FIFA23PlayerStats.csv", sep=",")

#Analysing Correlation between Age vs Potential,Overal and Potential, Overall vs Height, Weight
#sns.heatmap(playerStats.corr(), cbar=True, annot=True, cmap='Blues')
#plt.show()

#sns.barplot(data=playerStats, x='Grade', y='Overall')

#How Height and Weight Contribute to the Overalls of GRADE 4+ Players
"""
playerStats_4PLUS = playerStats[(playerStats['Grade'] == '4') | (playerStats['Grade'] == '5')]
sns.scatterplot(data=playerStats_4PLUS, x='HeightCM', y='WeightKG', hue='Grade', palette='deep', legend='brief')
plt.title("Height vs Weight Scatterplot")
plt.show()
"""