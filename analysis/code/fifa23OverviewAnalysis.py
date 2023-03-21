import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt

#importing the cleaned dataset
playerStats = pd.read_csv('cleaned-dataset/FIFA23PlayerStats.csv', index_col=0)
fig, axes = plt.subplots(2,2, figsize=(10,10), constrained_layout=True)

#Visualize the Player Stats on a broader scale

#Analysing Correlation between Age vs Potential,Overal and Potential, Overall vs Height, Weight
sns.heatmap(playerStats.corr(), cbar=True, annot=True, cmap='Blues', ax=axes[0,0]).set(title = "Correlation b/w Player Statistics")

#How Height and Weight Contribute to the Overalls of GRADE 4+ Players
playerStats_4PLUS = playerStats[(playerStats['Grade'] >= 4)]
sns.scatterplot(data=playerStats_4PLUS, x='HeightCM', y='WeightKG', hue='Grade', palette='deep', legend='brief', ax=axes[0,1]).set(title="Height vs Weight Scatterplot of Grade 4+ Players")

#Analysing Player Distribution wrt. Age
sns.kdeplot(x=playerStats['Age'], ax=axes[1,0]).set(title="Distribution of Players wrt Age")

#Analysing Player Distribution wrt Grade
sns.violinplot(x=playerStats['Grade'], ax=axes[1,1]).set(title="Distribution of Players wrt Grade", ylabel="Number of Players")

#Displaying the Plots
plt.savefig('analysis/Overview Analysis of Player Stats.png')
