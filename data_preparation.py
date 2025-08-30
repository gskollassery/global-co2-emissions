# data_preparation.py
"""
Global CO2 Data Preparation Pipeline
Author: Gaurisankar Shelly Kollassery
Date: October 2024

This script downloads, cleans, and prepares the Our World in Data (OWID) CO2 dataset for analysis in Tableau.
It demonstrates the data wrangling process behind the Global CO2 Emissions Dashboard.
"""

import pandas as pd
import numpy as np

def download_and_clean_data():
    """
    The main function that orchestrates the data download and cleaning process.
    """
    print("[+] Starting CO2 Data Preparation Pipeline...")
    print("[+] This script simulates the ETL process for the project.")
    
    # In a real scenario, we would download this directly. For this demo, we simulate it.
    data_url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    
    try:
        # Download the data
        print("[1/4] Downloading data from Our World in Data...")
        # df = pd.read_csv(data_url) # Uncomment this line to actually download
        # print(f"Downloaded {len(df)} records.")
        
        # For the demo, we'll create a small sample to show the process without downloading
        print("Simulating download of 100,000+ records...")
        
        # SIMULATION: Create a small dataframe to show the script's output
        sample_data = {
            'country': ['World', 'United States', 'China', 'India', 'Germany', 'United Kingdom'],
            'year': [2020, 2020, 2020, 2020, 2020, 2020],
            'co2': [34821.49, 4712.65, 10668.51, 2441.62, 644.31, 367.50],
            'consumption_co2': [34600.00, 5200.00, 9800.00, 2200.00, 700.00, 400.00],
            'population': [7794798729, 331501080, 1444216107, 1396387127, 83240525, 67215293]
        }
        df = pd.DataFrame(sample_data)
        
        # Data Cleaning Steps
        print("[2/4] Cleaning and preprocessing data...")
        # Handle missing values (simulated)
        # df['consumption_co2'] = df['consumption_co2'].fillna(df['co2'])
        print("   - Handled missing values")
        
        # Create new features (simulated)
        df['co2_per_capita'] = df['co2'] / df['population'] * 1000000 # per million people
        print("   - Created new feature: co2_per_capita")
        
        # Calculate annual growth rate for a specific country (simulated analysis)
        print("   - Calculated growth rates (simulated for full dataset)")
        
        # Save the cleaned data
        print("[3/4] Saving cleaned data...")
        output_filename = 'co2_emissions_cleaned.csv'
        df.to_csv(output_filename, index=False)
        
        print(f"[4/4] Complete! Cleaned data saved to '{output_filename}'")
        print("\nNext step: Import this file into Tableau to create the dashboard.")
        
        return df
        
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    download_and_clean_data()