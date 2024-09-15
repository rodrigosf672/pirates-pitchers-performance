
# Pittsburgh Pirates Pitcher Performance Analysis

## Project Overview
This project conducts exploratory data analysis (EDA) and binary classification of Pittsburgh Pirates pitchers. It leverages physical and performance metrics such as ERA, strikeouts, WHIP, age, height, and weight to classify pitchers into high or low performers. The project includes data extraction, processing, visualization, and the use of a machine learning model (Random Forest) to predict pitcher performance.

## Key Features
- **Data Collection**: Pulls career pitching statistics from the MLB Stats API for selected Pittsburgh Pirates pitchers.
- **Exploratory Data Analysis (EDA)**: Visualizes key performance metrics and correlations between them.
- **Binary Classification**: Implements a Random Forest classifier to categorize pitchers into high and low performers based on ERA.
- **Feature Importance**: Identifies key metrics driving high performance in pitchers.

## Motivation
The motivation behind this project is to demonstrate data science and machine learning skills in the context of sports analytics, focusing on the Pittsburgh Pirates' pitching staff. The goal is to classify pitchers based on their physical attributes and performance metrics to provide valuable insights into player development.

## Technologies Used
- **Programming Languages**: Python
- **Libraries**:
  - `requests` (for API calls)
  - `pandas` (for data manipulation)
  - `seaborn`, `matplotlib` (for visualization)
  - `scikit-learn` (for machine learning)
- **ML Model**: Random Forest Classifier (for binary classification)
- **Data Sources**: 
  - **MLB Stats API**: Provides pitcher performance data and metrics such as ERA, strikeouts, WHIP, and innings pitched.
  - **Pittsburgh Pirates Website**: Provides data on pitcher characteristics such as age, weight, and height.

## Installation and Setup

### Prerequisites:
- Python 3.x
- Install required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Analysis:
1. **Clone this repository**:
   ```bash
   git clone https://github.com/rodrigosf672/pirates-pitchers-performance.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd pirates-pitchers-performance
   ```
3. **Run the scripts to collect data from the MLB Stats API and to create data frames for each pitcher as CSV files**:
   ```bash
   python Script01-player_performance.py
   ```
   ```bash
   python Script02-data_frame_pitchers.py
   ```
   Script01 will retrieve pitchers' performance data from the API, and Script02 will clean and organize the data as CSV files, along with characteristics retrieved from the Pittsburgh Pirates website.
   
4. **Run the script to perform exploratory data analysis**:
   ```bash
   python Script03-exploratory_data_analysis.py
   ```

5. **Run the script to categorize pitchers based on performance**:
   ```bash
   python Script04-performance_categorizer.py
   ```
   The script will generate:
   - Confusion matrix of the classification results.
   - Feature importance plot showing the most relevant factors contributing to pitcher performance.

## Output Organization

After running the scripts, the generated output files (e.g., CSVs, plots) will be saved in the root directory. To maintain an organized project structure, it is recommended to manually move these files into the following folder structure:

### Folder Structure:
```
/outputs/
    a) players_pitchers_stats/ (CSV files from Scripts 01 and 02)
        - Bailey_Falter_stats.csv
        - Colin_Holderman_stats.csv
        - David_Bednar_stats.csv
        - Dennis_Santana_stats.csv
        - Isiah_Kiner-Falefa_stats.csv
        - Jalen_Beeks_stats.csv
        - Luis_L._Ortiz_stats.csv
        - Rowdy_Tellez_stats.csv
        - Ryan_Borucki_stats.csv

    b) exploratory_data_analysis/ (Plots from Script 03)
        - age_vs_era.png
        - heatmap_physical_vs_performance.png
        - height_vs_strikeouts.png
        - pairplot_physical_vs_performance.png
        - weight_vs_innings_pitched.png

    c) binary_classification/ (Plots from Script 04)
        - confusion_matrix.png
        - feature_importance.png
```

### Steps to Manually Organize the Outputs:

1. **Create the following directories inside the `/outputs/` folder**:
   - `players_pitchers_stats/` for storing CSV files generated from Scripts 01 and 02.
   - `exploratory_data_analysis/` for storing plots generated from Script 03.
   - `binary_classification/` for storing plots generated from Script 04.

2. **Move Files**:
   - Move all CSV files (e.g., pitcher stats) to the `players_pitchers_stats/` folder.
   - Move all plots generated from exploratory data analysis (EDA) to the `exploratory_data_analysis/` folder.
   - Move plots generated from the binary classification process (e.g., confusion matrix, feature importance) to the `binary_classification/` folder.

## Features Breakdown
- **Data Collection**: Retrieves and filters pitcher statistics, saving them as CSV files.
- **EDA and Visualization**:
  - Visualizes performance metrics such as ERA, strikeouts, WHIP, etc.
  - Correlates physical attributes (age, height, weight) with pitching performance.
- **Binary Classification**:
  - Categorizes pitchers into high and low performers based on ERA (<3.5 is a high performer, >=3.5 is a low performer).
  - Uses a Random Forest classifier to predict performance.
  - Evaluates the model using accuracy, precision, recall, and confusion matrix.
- **Feature Importance**: Ranks features based on their contribution to predicting pitcher performance.

## Insights and Conclusions
Based on the analysis and outputs generated from the project, the following conclusions can be drawn:
1. **Pitcher Performance Correlation**: Pitchers with a lower ERA (<3.5) generally had higher strikeout rates and lower WHIP values, indicating strong performance in preventing runs and managing base runners.
2. **Physical Attributes vs. Performance**: Age and height did not show a significant correlation with overall pitching performance, while weight had a moderate positive correlation with innings pitched, suggesting heavier pitchers tend to pitch longer.
3. **Feature Importance**: The Random Forest classifier identified WHIP and strikeouts as the most important factors in classifying high vs. low performers, with WHIP having the strongest influence.
4. **Classification**: The binary classification model herein reported aimed to establish a baseline for future analyses, hence why maximum accuracy was achieved. In the future, adding data from other pitchers would be helpful to determine the classification accuracy of this model. It is also relevant to consider that the data used here was from 10 pitchers only, which is very limiting. 
5. **Areas for Improvement**: Further enhancements could include integrating more advanced metrics, such as pitch velocity and type, to improve classification accuracy and gain deeper insights into performance drivers.
These conclusions provide valuable insights into the factors influencing pitcher performance for the Pittsburgh Pirates, which can be useful for player development and decision-making in team management.

## Future Enhancements
- Integrate additional pitcher performance metrics such as pitch type and velocity.
- Upon introduction of additional data and determination of classification accuracy, it could be helpful to experiment with more advanced machine learning models like XGBoost or SVM to improve classification accuracy.
- Add time-series forecasting to predict future pitcher performance based on historical data.

## How to Contribute
1. **Fork this repository**.
2. **Create a new branch for your feature**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes and push them to the branch**:
   ```bash
   git commit -m "Add a new feature"
   git push origin feature-branch
   ```
4. **Submit a Pull Request (PR)**.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or suggestions, feel free to reach out to me at [rodrigosf672@gmail.com](mailto:rodrigosf672@gmail.com).
