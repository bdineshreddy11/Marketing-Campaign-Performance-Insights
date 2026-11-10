import os
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv"

# 1. Load the dataset
try:
  df = pd.read_csv(DATA_URL)
  print("✓ Dataset successfully loaded from URL.")
except Exception as e:
  print(f"URL load failed ({e}). Loading from local backup if present...")
  df = pd.read_csv("marketing_campaign.csv")

# 2. Data Cleaning & Normalization
# Strip column name whitespaces
df.columns = df.columns.str.strip()

# Standardize Channel naming variation if present
if "Channel_Used" in df.columns and "Channels_Used" not in df.columns:
  df.rename(columns={"Channel_Used": "Channels_Used"}, inplace=True)

# Clean Acquisition_Cost: remove currency symbols like '$' or commas, convert to numeric
if df["Acquisition_Cost"].dtype == object:
  df["Acquisition_Cost"] = (
      df["Acquisition_Cost"]
      .astype(str)
      .str.replace("$", "", regex=False)
      .str.replace(",", "", regex=False)
      .str.strip()
      .astype(float)
  )

# Parse Date column to standard datetime format
if "Date" in df.columns:
  df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Drop complete duplicate records if any exist
df.drop_duplicates(inplace=True)

# 3. Export Cleaned Dataset for File 2
CLEANED_CSV_PATH = "cleaned_marketing_campaign.csv"
df.to_csv(CLEANED_CSV_PATH, index=False)
print(f"✓ Cleaned dataset saved locally as: '{CLEANED_CSV_PATH}'\n")

# PART 2: DESCRIPTIVE ANALYSIS 
# Basic Structure
print("\n--- 2.1 First 5 Rows of Dataset ---")
print(df.head())

print("\n--- 2.2 Dataset Dimensions ---")
print(f"Total Rows:    {df.shape[0]:,}")
print(f"Total Columns: {df.shape[1]}")

print("\n--- 2.3 Concise Summary (Data Types and Non-Null Counts) ---")
df.info()

print("\n--- 2.4 Descriptive Statistics for Numerical Columns ---")
print(df.describe().T)

# Data Exploration

print(f"\nUnique Campaign_ID count: {df['Campaign_ID'].nunique():,}")

print(f"\nUnique Location values ({df['Location'].nunique()} unique):")
print(df["Location"].dropna().unique().tolist())

print(
    f"\nUnique Customer_Segment values ({df['Customer_Segment'].nunique()} unique):"
)
print(df["Customer_Segment"].dropna().unique().tolist())

print("\nOccurrences of each category in 'Campaign_Type':")
print(df["Campaign_Type"].value_counts())

channel_col = (
    "Channels_Used" if "Channels_Used" in df.columns else "Channel_Used"
)
print(f"\nOccurrences of each category in '{channel_col}':")
print(df[channel_col].value_counts())

