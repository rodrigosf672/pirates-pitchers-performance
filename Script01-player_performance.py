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
This script pulls career pitching statistics for selected Pittsburgh Pirates
pitchers from the MLB Stats API, processes the data, and saves it in a structured
format (CSV files). It focuses on collecting key performance metrics such as ERA,
strikeouts, WHIP, and innings pitched for further analysis.
'''

import requests
import pandas as pd
import time

# List of players with relevant IDs
players = [
    {"name": "David Bednar", "id": 676701},
    {"name": "Jalen Beeks", "id": 668678},
    {"name": "Ryan Borucki", "id": 669211},
    {"name": "Aroldis Chapman", "id": 547973},
    {"name": "Bailey Falter", "id": 670950},
    {"name": "Colin Holderman", "id": 670032},
    {"name": "Jared Jones", "id": 682993},
    {"name": "Mitch Keller", "id": 669354},
    {"name": "Carmen Mlodzinski", "id": 682998},
    {"name": "Kyle Nicolas", "id": 686837},
    {"name": "Luis L. Ortiz", "id": 664126},
    {"name": "Dennis Santana", "id": 661395},
    {"name": "Paul Skenes", "id": 702481},
    {"name": "Joey Wentz", "id": 663891},
    {"name": "Joey Bart", "id": 663698},
    {"name": "Yasmani Grandal", "id": 518735},
    {"name": "Billy Cook", "id": 676072},
    {"name": "Oneil Cruz", "id": 666176},
    {"name": "Nick Gonzales", "id": 676999},
    {"name": "Connor Joe", "id": 657824},
    {"name": "Isiah Kiner-Falefa", "id": 643396},
    {"name": "Rowdy Tellez", "id": 642133},
    {"name": "Jared Triolo", "id": 682998},
    {"name": "Alika Williams", "id": 683278},
    {"name": "Bryan De La Cruz", "id": 673490},
    {"name": "Andrew McCutchen", "id": 457705},
    {"name": "Bryan Reynolds", "id": 668804},
    {"name": "Michael A. Taylor", "id": 621035}
]

# API call
def get_player_stats(player_id):
    url = f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats?stats=career&group=pitching"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve stats for player ID: {player_id}")
        return None

# Filter the important columns
important_columns = [
    'gamesPlayed', 'gamesStarted', 'wins', 'losses', 'era', 'inningsPitched',
    'strikeOuts', 'whip', 'strikeoutWalkRatio', 'homeRunsPer9', 'saves'
]

# Loop through each player
for player in players:
    stats_data = get_player_stats(player['id'])
    
    if stats_data and 'stats' in stats_data and len(stats_data['stats']) > 0:
        if 'splits' in stats_data['stats'][0] and len(stats_data['stats'][0]['splits']) > 0:
            # Extract stats
            stats = stats_data['stats'][0]['splits'][0]['stat']
            
            # Convert stats to a DataFrame and filter columns
            df = pd.DataFrame([stats])[important_columns]
            
            # Save to CSV
            filename = f"{player['name'].replace(' ', '_')}_stats.csv"
            df.to_csv(filename, index=False)
            
            print(f"Saved filtered stats for {player['name']} to {filename}")
        else:
            print(f"No splits data available for {player['name']}")
    else:
        print(f"No stats data available for {player['name']}")
    
    # Pauses between API calls (to prevent excessive requests)
    time.sleep(1)
