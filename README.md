# 📊 Marketing Campaign Performance Insights

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Matplotlib-Charts-orange?style=for-the-badge" />
</p>

<p align="center">
  <b>An Exploratory Data Analysis Project Using Python</b>
</p>

---

## 📌 Project Overview

Marketing Campaign Performance Insights is a data analysis project that focuses on evaluating the performance of different marketing campaigns across companies, channels, customer segments, languages, and geographical locations.

The project uses Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn to explore campaign data, calculate important performance metrics, and create visualizations.

The analysis helps understand campaign effectiveness, customer engagement, acquisition costs, conversion rates, and return on investment (ROI). The findings can help businesses identify successful marketing strategies and make better decisions for future campaigns.

## 🎯 Problem Statement

In the competitive digital marketing environment, understanding campaign performance is important for improving marketing results and managing advertising expenses. Although companies collect large amounts of campaign data, comparing performance across different channels, campaign types, customer segments, and locations can be challenging.

This project analyzes marketing campaign data to understand conversion rates, acquisition costs, engagement scores, and return on investment. It also examines customer behavior, geographical differences, and performance trends over time to identify successful campaigns and provide useful insights for improving future marketing strategies.

## 📂 Dataset Information

| Attribute | Details |
|---|---|
| Dataset Name | Marketing Campaign Dataset |
| File Format | CSV |
| Data Source | GitHub |
| Analysis Type | Descriptive Analysis and EDA |
| Programming Language | Python |

**Dataset Link:**

[Download Marketing Campaign Dataset](https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv)

### Data Dictionary

| Column Name | Description |
|---|---|
| Campaign_ID | Unique identifier for each campaign |
| Company | Organization running the campaign |
| Campaign_Type | Type of marketing campaign |
| Target_Audience | Demographic group targeted |
| Duration | Campaign duration in days |
| Channels_Used | Marketing channels used |
| Conversion_Rate | Percentage of successful conversions |
| Acquisition_Cost | Cost incurred to acquire a customer |
| ROI | Return on Investment |
| Location | Geographical campaign location |
| Language | Language used in campaign content |
| Clicks | Total number of clicks |
| Impressions | Total number of campaign views |
| Engagement_Score | Customer engagement score from 1 to 10 |
| Customer_Segment | Category of customers targeted |
| Date | Date of campaign |

## 🛠️ Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| Pandas | Data loading, manipulation, and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook / VS Code | Development environment |

## 📁 Project Folder Structure

```text
marketing_campaign_project/
│
├── 01_data_loading_and_descriptive_analysis.py
├── 02_eda_and_visualizations.py
├── cleaned_marketing_campaign.csv
│
├── eda_plots/
│   ├── 01_scatter_acquisition_vs_roi.png
│   ├── 02_bar_conversion_channel_by_campaign.png
│   ├── 03_box_engagement_by_campaign_type.png
│   ├── 04_bar_avg_roi_by_company.png
│   ├── 05_heatmap_engagement_vs_conversion.png
│   ├── 06_count_target_audience.png
│   ├── 07_bar_segment_conversion_by_language.png
│   ├── 08_box_acquisition_by_segment_and_channel.png
│   ├── 09_bar_conversion_by_language.png
│   ├── 10_bar_engagement_channel_by_campaign.png
│   ├── 11_pie_total_roi_by_channel.png
│   ├── 12_scatter_clicks_vs_impressions.png
│   ├── 13_hist_duration.png
│   ├── 14_line_conversion_trend_by_company.png
│   ├── 15_line_engagement_score_trend.png
│   ├── 16_bar_acquisition_cost_by_location.png
│   ├── 17_bar_conversion_location_audience.png
│   └── 18_pie_proportion_roi_by_location.png
│
└── README.md
```

## ⚙️ Project Implementation

### Step 1: Data Loading and Descriptive Analysis

The first Python script loads the marketing campaign dataset into a Pandas DataFrame and performs initial data exploration.

**Activities performed:**

- Load the CSV dataset using Pandas.
- Display the first few records.
- Identify the number of rows and columns.
- Check column names, data types, and non-null values.
- Generate descriptive statistics for numerical columns.
- Count unique Campaign_ID values.
- Identify unique locations and customer segments.
- Calculate the frequency of campaign types and marketing channels.
- Perform the cleaning operations implemented in the script.
- Export the cleaned dataset as a CSV file.

**Output:** `cleaned_marketing_campaign.csv`

### Step 2: Exploratory Data Analysis (EDA) and Visualization

The second Python script uses the cleaned dataset to perform exploratory analysis and generates 18 charts.

The visualizations are divided into five major categories.

## 📈 Data Visualization and Analysis

### 1. Campaign Performance Analysis

This section examines the performance and profitability of different marketing campaigns.

**Visualizations:**

1. Acquisition Cost vs ROI – Scatter Plot
2. Average Conversion Rate by Channel and Campaign Type – Bar Chart
3. Engagement Score by Campaign Type – Box Plot
4. Average ROI by Company – Bar Chart
5. Engagement Score vs Conversion Rate – Correlation Heatmap

### 2. Customer Segmentation Analysis

This section explores customer groups and their responses to marketing campaigns.

**Visualizations:**

6. Target Audience Distribution – Count Plot
7. Customer Segment Conversion Rate by Language – Bar Chart
8. Acquisition Cost by Customer Segment and Channel – Box Plot
9. Average Conversion Rate by Language – Bar Chart

### 3. Channel Effectiveness Analysis

This section compares the effectiveness of different marketing channels.

**Visualizations:**

10. Engagement Score by Channel and Campaign Type – Bar Chart
11. Total ROI by Marketing Channel – Pie Chart
12. Clicks vs Impressions by Channel – Scatter Plot

### 4. Time-Based Analysis

This section examines campaign duration and performance trends over time.

**Visualizations:**

13. Campaign Duration Distribution – Histogram
14. Conversion Rate Trend by Company – Line Chart
15. Engagement Score Trend Over Time – Line Chart

### 5. Geographic Analysis

This section explores geographical differences in campaign costs and performance.

**Visualizations:**

16. Acquisition Cost by Location – Bar Chart
17. Conversion Rate by Location and Target Audience – Bar Chart
18. ROI Distribution by Location – Pie Chart

---

## 🖼️ Visualization Gallery

The following charts are generated by the EDA script and saved inside the `eda_plots/` directory.

**1. Campaign Performance Analysis**

| Chart 01 | Chart 02 |
|:---:|:---:|
| **Acquisition Cost vs ROI** | **Conversion Rate by Channel and Campaign** |
| <img src="Marketing%20Campaign/eda_plots/01_scatter_acquisition_vs_roi.png" width="100%"> | <img src="Marketing%20Campaign/eda_plots/02_bar_conversion_channel_by_campaign.png" width="100%" alt="Conversion Rate by Channel and Campaign Type"/> 

| Chart 03 | Chart 04 |
|:---:|:---:|
| **Engagement Score by Campaign Type** | **Average ROI by Company** |
<img src="Marketing%20Campaign/eda_plots/03_box_engagement_by_campaign_type.png" width="100%" alt="Engagement Score by Campaign Type"/> | <img src="Marketing%20Campaign/eda_plots/04_bar_avg_roi_by_company.png" width="100%" alt="Average ROI by Company"/>|

| Chart 05 |
|:---:|
| **Engagement Score vs Conversion Rate – Correlation Heatmap** |
| <img src="Marketing%20Campaign/eda_plots/05_heatmap_engagement_vs_conversion.png" width="75%" alt="Engagement and Conversion Correlation Heatmap"/> |
**2. Customer Segmentation Analysis**

| Chart 06 | Chart 07 |
|:---:|:---:|
| **Target Audience Distribution** | **Segment Conversion Rate by Language** |
| <img src="Marketing%20Campaign/eda_plots/06_count_target_audience.png" width="100%" alt="Target Audience Distribution"/> | <img src="Marketing%20Campaign/eda_plots/07_bar_segment_conversion_by_language.png" width="100%" alt="Segment Conversion Rate by Language"/> |
|Chart 08 | Chart 09 |
|:---:|:---:|
| **Acquisition Cost by Segment and Channel** | **Average Conversion Rate by Language** |
| <img src="Marketing%20Campaign/eda_plots/08_box_acquisition_by_segment_and_channel.png" width="100%" alt="Acquisition Cost by Segment and Channel"/> | <img src="Marketing%20Campaign/eda_plots/09_bar_conversion_by_language.png" width="100%" alt="Average Conversion Rate by Language"/> |

**3. Channel Effectiveness Analysis**

| Chart 10 | Chart 11 |
|:---:|:---:|
| **Engagement by Channel and Campaign Type** | **Total ROI by Channel** |
| <img src="Marketing%20Campaign/eda_plots/10_bar_engagement_channel_by_campaign.png" width="100%" alt="Engagement by Channel and Campaign Type"/> | <img src="Marketing%20Campaign/eda_plots/11_pie_total_roi_by_channel.png" width="100%" alt="Total ROI by Channel"/> |

| Chart 12 |
|:---:|
| **Clicks vs Impressions by Channel** |
| <img src="Marketing%20Campaign/eda_plots/12_scatter_clicks_vs_impressions.png" width="75%" alt="Clicks vs Impressions by Channel"/> |

**4. Time-Based Analysis**

| Chart 13 | Chart 14 |
|:---:|:---:|
| **Campaign Duration Distribution** | **Conversion Rate Trend by Company** |
| <img src="Marketing%20Campaign/eda_plots/13_hist_duration.png" width="100%" alt="Campaign Duration Distribution"/> | <img src="Marketing%20Campaign/eda_plots/14_line_conversion_trend_by_company.png" width="100%" alt="Conversion Rate Trend by Company"/> |

| Chart 15 |
|:---:|
| **Engagement Score Trend Over Time** |
| <img src="Marketing%20Campaign/eda_plots/15_line_engagement_score_trend.png" width="75%" alt="Engagement Score Trend Over Time"/> |

**5. Geographic Analysis**

| Chart 16 | Chart 17 |
|:---:|:---:|
| **Acquisition Cost by Location** | **Conversion Rate by Location and Target Audience** |
|<img src="Marketing%20Campaign/eda_plots/16_bar_acquisition_cost_by_location.png" width="100%" alt="Acquisition Cost by Location"/> |<img src="Marketing%20Campaign/eda_plots/17_bar_conversion_location_audience.png" width="100%" alt="Conversion Rate by Location and Target Audience"/> |
|:---:|
| **ROI Distribution by Location** |
| <img src="Marketing%20Campaign/eda_plots/18_pie_proportion_roi_by_location.png" width="75%" alt="ROI Distribution by Location"/> |

---

## ▶️ How to Run the Project

### Prerequisites

Make sure Python is installed on your system.

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd marketing_campaign_project
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### 4. Run Data Loading and Descriptive Analysis

```bash
python 01_data_loading_and_descriptive_analysis.py
```

This script loads the original dataset, performs the implemented cleaning and descriptive analysis, and generates the cleaned CSV file.

### 5. Run Exploratory Data Analysis

```bash
python 02_eda_and_visualizations.py
```

This script reads the cleaned dataset and generates all 18 visualizations inside the `eda_plots/` folder.

---

## 💡 Business Objectives

The main objectives of this project are:

- Evaluate the performance of different marketing campaign types.
- Identify channels that generate better conversion rates and ROI.
- Compare acquisition costs across companies and locations.
- Understand customer engagement across different audience segments.
- Examine the relationship between campaign engagement and conversion rates.
- Analyze campaign performance trends over time.
- Identify geographical differences in marketing performance.
- Support better marketing decisions through data-driven insights.

## 📌 Expected Business Outcomes

The analysis is intended to help marketing teams:

- Identify profitable marketing channels.
- Understand which customer segments respond better to campaigns.
- Evaluate marketing expenses against campaign returns.
- Compare campaign performance across companies and locations.
- Improve future marketing strategies using historical campaign insights.

## 📚 Skills Demonstrated

- Python Programming
- Data Loading and Processing
- Data Cleaning
- Pandas DataFrame Operations
- NumPy Operations
- Descriptive Statistics
- Exploratory Data Analysis (EDA)
- Data Visualization
- Statistical Analysis
- Business Insights and Interpretation

## 👨‍💻 Author

**Data Analytics Portfolio Project**

<p align="center">
  <b>Marketing Campaign Performance Insights</b><br/>
  <i>Turning marketing data into meaningful business insights using Python.</i>
</p>

---
