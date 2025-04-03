Camera Dataset Analysis Project
===============================

Overview
--------
This Python project provides tools for analyzing and visualizing camera datasets. It includes functionality for data manipulation, filtering, statistical analysis, and visualization through a command-line interface (CLI).

Features
--------

Data Handling
- Loads camera data from a CSV file
- Handles missing values by replacing them with column medians
- Provides methods to filter data by release year and price
- Allows adding new camera entries to the dataset

Extended Functionality
- Retrieve camera details by model name (case-insensitive)
- Update camera prices by model name

Visualization
- Price distribution histogram
- Scatter plot of max resolution vs price

Command-Line Interface
- Interactive menu system for:
  - Viewing dataset statistics
  - Filtering data
  - Adding new cameras
  - Retrieving and updating camera information
  - Generating visualizations

Requirements
------------
- Python 3.x
- pandas
- matplotlib

Installation
------------
1. Clone this repository or download the project files
2. Ensure the 'camera_dataset.csv' file is in the same directory as the script
3. Install required packages:
   pip install pandas matplotlib

Usage
-----
Run the script:
python camera_project-v1.py

Follow the on-screen menu to interact with the dataset:

1. View Dataset Summary: See statistical overview of the data
2. Filter by Release Year: View cameras released between specified years
3. Filter by Price: View cameras below a specified price
4. Add a New Camera: Enter details to add a new camera to the dataset
5. Retrieve Camera Details: Search for cameras by model name
6. Update Camera Price: Modify the price of a specific camera model
7. Visualize Data: Choose between price distribution or resolution vs price plots
8. Exit: Quit the program

Data Structure
--------------
The dataset should contain the following columns (sample values shown):
- Model (string): "Canon PowerShot A10"
- Release date (int): 2001
- Max resolution (float): 1280
- Low resolution (float): 640
- Effective pixels (float): 1.3
- Zoom wide (W) (float): 35
- Zoom tele (T) (float): 105
- Normal focus range (float): 50
- Macro focus range (float): 10
- Storage included (float): 8
- Weight (inc. batteries) (float): 270
- Dimensions (float): 110
- Price (float): 299

Notes
-----
- The script automatically handles missing values by replacing them with column medians
- All numeric inputs should be entered as numbers (no currency symbols, etc.)
- Model name searches are case-insensitive
- Changes made during the session are not automatically saved to the CSV file
