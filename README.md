Used Car Data Cleaning and Analysis

A Python practice project that cleans 1,000 synthetic car listings and explores listed prices using three visualizations.

Tools

* Python
* Pandas and NumPy
* Seaborn and Matplotlib

Dataset

The original dataset contains 1,000 rows and 12 columns, including brand, model, year, price in AED, mileage, fuel, transmission, city and listing date.

The data was generated for learning and deliberately includes errors. It does not represent actual UAE market listings.

Cleaning Process

* Removed exact duplicate rows.
* Cleaned extra spaces and inconsistent capitalization.
* Corrected spelling mistakes and category abbreviations.
* Removed currency labels, commas and mileage units.
* Converted numeric and date columns.
* Marked invalid values as missing.
* Excluded records without usable prices.
* Kept conflicting listing IDs and extreme values aside for review.
* Standardized model names.

Missing year, mileage and date values were retained rather than replaced with guessed values.

Visualizations

1. Median listed price by brand: compares typical prices.
2. Mileage vs listed price: explores the relationship between mileage and price.
3. Car age vs listed price: explores the relationship between age and price.

Mileage was generated independently of price, so a clear relationship is not expected.

Project Files

File	Purpose
Main.py	Cleaning and visualization code
messy_car_listings_1000.csv	Original practice dataset
cleaned_car_listings.csv	Cleaned dataset

Run the Project

Install the required libraries:

pip install pandas numpy matplotlib seaborn

Keep the CSV files alongside Main.py, then run:

python Main.py

The CSV path in the script should point to messy_car_listings_1000.csv in your project folder.

Limitations

The cleaning thresholds are practice assumptions. Chart results describe this synthetic dataset and should not be interpreted as real market findings.

Learning Focus

This project practises data cleaning, type conversion, handling missing values, reviewing conflicting records and creating charts. It was completed with ChatGPT assistance for coding guidance and explanations.
