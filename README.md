# ZrockGold Music Analysis Project

Welcome to the ZrockGold Music Analysis Project! This project is part of the ZrockGold internship for data analysts and focuses on analyzing music listening data obtained directly from Spotify. The goal is to perform exploratory data analysis (EDA) and generate insights into music-listening behavior.

<img width="565" alt="image" src="https://github.com/Ayushmi-Adh/ZrockGold-Internship/assets/132826306/07ca4a77-bf60-4607-906e-224dceb0704c">


## Table of Contents:

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Overview:

This project aims to analyze Spotify music listening data to gain insights into user preferences, popular artists, top songs, and trends in listening behavior. The analysis includes data loading, cleaning, analysis, and visualization tasks.

## Project Structure:

The project is structured as follows:
- `main.py`: Main script that coordinates data loading, analysis, and visualization tasks.
- `data_loader.py`: Module for loading and preprocessing Spotify data.
- `data_analysis.py`: Module for performing data analysis tasks.
- `data_visualization.py`: Module for creating visualizations based on analysis results.
- `spotify_data.json`: Sample Spotify data file for testing.

## Getting Started:

To get started with the project, follow these steps:
1. Clone the repository to your local machine using Git:
   ```
   git clone https://github.com/Ayushmi-Adh/ZrockGold-Internship.git
   ```
2. Navigate to the project directory:
   ```
   cd ZrockGold-Internship
   ```

## Usage:

To run the project:
1. Place your Spotify data export file (CSV or Excel) in the project directory.
2. Update the data file path in `main.py` if necessary.
3. Install the required dependencies using `pip`:
   ```
   pip install -r requirements.txt
   ```
4. Run the main Python script to perform data analysis and generate visualizations:
   ```
   python main.py
   ```

## Dependencies:

The project requires the following dependencies:
- Python 3. x
- Pandas
- Matplotlib
- Seaborn

Install these dependencies using `pip`:
```
pip install pandas matplotlib seaborn
```


