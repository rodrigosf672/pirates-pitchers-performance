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
This script implements a machine learning classifier (Random Forest) to categorize
pitchers into high and low performers based on key metrics such as ERA and strikeouts.
It evaluates the model’s accuracy using classification metrics like precision, recall,
and confusion matrices and determines feature importance in predicting performance.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

pitchers_df = pd.read_csv('all_pitchers_with_stats.csv')

# Convert Date of Birth (DOB) to age
current_year = datetime.now().year
pitchers_df['DOB'] = pd.to_datetime(pitchers_df['DOB'])
pitchers_df['age'] = current_year - pitchers_df['DOB'].dt.year

# Convert height to inches
def height_to_inches(height_str):
    feet, inches = height_str.split("'")
    return int(feet) * 12 + int(inches.replace('"', ''))

pitchers_df['Ht_inches'] = pitchers_df['Ht'].apply(height_to_inches)

# Step 1: Categorize pitchers into high/low performers based on ERA
# ERA threshold: < 3.5 is high performer (1), >= 3.5 is low performer (0)
pitchers_df['performance'] = (pitchers_df['era'] < 3.5).astype(int)

# Step 2: Select relevant features (physical characteristics and performance stats)
X = pitchers_df[['age', 'Ht_inches', 'Wt', 'inningsPitched', 'strikeOuts', 'whip']]

# Target: Performance classification (1: High performer, 0: Low performer)
y = pitchers_df['performance']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = clf.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap='Blues', xticklabels=["Low Performer", "High Performer"], yticklabels=["Low Performer", "High Performer"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig('confusion_matrix.png', dpi=300)
plt.show()

# Step 7: Feature Importances
feature_importances = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nFeature Importances:")
print(feature_importances)

# Plot feature importances
plt.figure(figsize=(8,6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.title("Feature Importances")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.savefig('feature_importance.png', dpi=300)
plt.show()