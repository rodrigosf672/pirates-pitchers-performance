''' 
Project: Pittsburgh Pirates' Pitchers Performance - Analysis and Classification
Author: Rodrigo Silva Ferreira
Created on: September 15, 2024.

Objective: To perform exploratory data analysis (EDA) and machine learning
classification of Pittsburgh Pirates' pitchers based on their physical and
performance metrics, such as ERA, strikeouts, WHIP, age, height, and weight. 
The goal is to identify key factors influencing high and low performance to
aid in player development and decision-making.

Specific goal of this script:
This script performs exploratory data analysis (EDA) on the collected data.
It visualizes key performance metrics and their correlations, identifies trends,
outliers, and relationships between physical and performance attributes to gain
insights into Pittsburgh Pirates pitchers' overall performance.
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data
pitchers_df = pd.read_csv('all_pitchers_with_stats.csv')

# Convert Date of Birth (DOB) to Age
current_year = datetime.now().year
pitchers_df['DOB'] = pd.to_datetime(pitchers_df['DOB'])
pitchers_df['age'] = current_year - pitchers_df['DOB'].dt.year

# Convert height to inches for easier analysis
def height_to_inches(height_str):
    feet, inches = height_str.split("'")
    return int(feet) * 12 + int(inches.replace('"', ''))

pitchers_df['Ht_inches'] = pitchers_df['Ht'].apply(height_to_inches)

# 1. Summary Statistics
print("Summary Statistics:")
print(pitchers_df.describe())

# 2. Correlation Matrix - Focus on physical attributes vs performance
correlation_matrix = pitchers_df[['age', 'Ht_inches', 'Wt', 'inningsPitched', 'strikeOuts', 'whip', 'era']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# 3. Visualizations - Focused on how physical characteristics affect performance

# Age vs ERA (scatter plot with regression line)
plt.figure(figsize=(8,6))
sns.regplot(x='age', y='era', data=pitchers_df, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('Age vs ERA')
plt.xlabel('Age')
plt.ylabel('ERA')
plt.savefig('age_vs_era.png', dpi=300)
plt.show()

# Height vs Strikeouts
plt.figure(figsize=(8,6))
sns.regplot(x='Ht_inches', y='strikeOuts', data=pitchers_df, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('Height vs Strikeouts')
plt.xlabel('Height (in inches)')
plt.ylabel('Strikeouts')
plt.savefig('height_vs_strikeouts.png', dpi=300)
plt.show()

# Weight vs Innings Pitched
plt.figure(figsize=(8,6))
sns.regplot(x='Wt', y='inningsPitched', data=pitchers_df, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('Weight vs Innings Pitched')
plt.xlabel('Weight (lbs)')
plt.ylabel('Innings Pitched')
plt.savefig('weight_vs_innings_pitched.png', dpi=300)
plt.show()

# 4. Pairplot - Focusing on Physical Characteristics and Performance
sns.pairplot(pitchers_df[['age', 'Ht_inches', 'Wt', 'inningsPitched', 'strikeOuts', 'whip', 'era']])
plt.savefig('pairplot_physical_vs_performance.png', dpi=300)
plt.show()

# 5. Heatmap for Correlation Matrix - Physical characteristics vs performance metrics
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix: Physical Characteristics vs Performance')
plt.savefig('heatmap_physical_vs_performance.png', dpi=300)
plt.show()