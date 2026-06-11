# 📘 Assignment: Data Pipelines with Python

## 🎯 Objective

Build a Python data pipeline that reads CSV data, cleans and transforms it, and saves the processed results to a new file.

## 📝 Tasks

### 🛠️ Load and Inspect Data

#### Description
Load the provided CSV dataset and explore the structure and contents of the data.

#### Requirements
Completed program should:

- Load `sales_data.csv` using Python
- Print the number of rows and columns
- Display the first 5 rows of the dataset
- Identify any missing or invalid values in important columns

### 🛠️ Clean and Transform Data

#### Description
Clean the dataset and compute a useful new field for analysis.

#### Requirements
Completed program should:

- Remove rows with missing or invalid values for `quantity` or `price`
- Convert `quantity` to integers and `price` to floats
- Add a new column `total_sales` computed as `quantity * price`
- Print a summary showing total sales across all records

### 🛠️ Save Processed Results

#### Description
Save the cleaned and transformed data to a new CSV file and summarize the results.

#### Requirements
Completed program should:

- Save the cleaned dataset with the `total_sales` column to `processed_sales.csv`
- Print the number of rows saved
- Print the product with the highest total sales
