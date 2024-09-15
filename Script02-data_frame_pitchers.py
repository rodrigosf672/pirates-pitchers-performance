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
This script combines individual pitcher statistics into a unified data frame,
consolidating the CSV files generated from the previous script. It also includes
additional pitcher attributes (e.g., age, height, weight) and prepares the data
for exploratory data analysis (EDA) and modeling.
'''

import pandas as pd
import glob

# Path to CSV files
path = "*.csv"

# Use glob to get all the CSV file names
csv_files = glob.glob(path)

# Initialize an empty list to hold dataframes
df_list = []

# Loop through the files and read them into pandas DataFrames
for file in csv_files:
    df = pd.read_csv(file)
    # Add a column with the player name by extracting from the filename
    df['player_name'] = file.split('_stats.csv')[0].split('/')[-1].replace('_', ' ')
    df_list.append(df)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(df_list, ignore_index=True)

# Filter to include only pitchers
pitcher_names = [
    "David Bednar", "Jalen Beeks", "Ryan Borucki", 
    "Aroldis Chapman", "Bailey Falter", "Colin Holderman", 
    "Luis L. Ortiz", "Dennis Santana"
]

pitchers_df = combined_df[combined_df['player_name'].isin(pitcher_names)].copy()

# Add additional information (B/T, Height, Weight, DOB) for pitchers, extracted from Pirates' website.
pitcher_stats = {
    "David Bednar": {"B/T": "L/R", "Ht": "6'0\"", "Wt": 225, "DOB": "10/10/1994"},
    "Jalen Beeks": {"B/T": "L/L", "Ht": "5'11\"", "Wt": 215, "DOB": "07/10/1993"},
    "Ryan Borucki": {"B/T": "L/L", "Ht": "6'4\"", "Wt": 210, "DOB": "03/31/1994"},
    "Aroldis Chapman": {"B/T": "L/L", "Ht": "6'4\"", "Wt": 235, "DOB": "02/28/1988"},
    "Bailey Falter": {"B/T": "R/L", "Ht": "6'4\"", "Wt": 205, "DOB": "04/24/1997"},
    "Colin Holderman": {"B/T": "R/R", "Ht": "6'4\"", "Wt": 230, "DOB": "10/08/1995"},
    "Luis L. Ortiz": {"B/T": "R/R", "Ht": "6'2\"", "Wt": 235, "DOB": "01/27/1999"},
    "Dennis Santana": {"B/T": "R/R", "Ht": "6'2\"", "Wt": 190, "DOB": "04/12/1996"}
}

# Map additional stats to pitchers
pitchers_df['B/T'] = pitchers_df['player_name'].map(lambda x: pitcher_stats.get(x, {}).get('B/T'))
pitchers_df['Ht'] = pitchers_df['player_name'].map(lambda x: pitcher_stats.get(x, {}).get('Ht'))
pitchers_df['Wt'] = pitchers_df['player_name'].map(lambda x: pitcher_stats.get(x, {}).get('Wt'))
pitchers_df['DOB'] = pitchers_df['player_name'].map(lambda x: pitcher_stats.get(x, {}).get('DOB'))

# Display the first few rows of the updated dataframe
print(pitchers_df.head())

# Save the updated dataframe to a CSV file for future use
pitchers_df.to_csv('all_pitchers_with_stats.csv', index=False)
