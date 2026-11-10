
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visual configurations
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 11, "figure.autolayout": True})

# step 1 cleaned data file path

DATA_FILE = "cleaned_marketing_campaign.csv"

if not os.path.exists(DATA_FILE):
    print(f"ERROR: '{DATA_FILE}' was not found!")
    print("Please run '01_data_loading_and_descriptive_analysis.py' first.")
    sys.exit(1)

df = pd.read_csv(DATA_FILE)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

channel_col = "Channels_Used" if "Channels_Used" in df.columns else "Channel_Used"
print(f"✓ Loaded {len(df):,} cleaned rows successfully.\n")

# Set output directory for plots
OUTPUT_DIR = "eda_plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"Plots will be saved directly into: '{OUTPUT_DIR}/'\n")

# 3 campaign performance::
print("Generating Campaign Performance charts...")

# 1. Scatter Plot: Acquisition_Cost vs. ROI
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Acquisition_Cost",
    y="ROI",
    hue="Campaign_Type",
    alpha=0.7,
    palette="tab10",
)
plt.title("Relationship Between Acquisition Cost and ROI", fontsize=13, pad=12)
plt.xlabel("Acquisition Cost ($)")
plt.ylabel("Return on Investment (ROI)")
plt.savefig(
    os.path.join(OUTPUT_DIR, "01_scatter_acquisition_vs_roi.png"),
    bbox_inches="tight",
)
plt.close()

# 2. Bar Chart: Average Conversion_Rate by Channel_Used categorized by Campaign_Type
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x=channel_col,
    y="Conversion_Rate",
    hue="Campaign_Type",
    errorbar=None,
    palette="muted",
)
plt.title(
    f"Average Conversion Rate by {channel_col} Categorized by Campaign Type",
    fontsize=13,
    pad=12,
)
plt.xlabel("Channel Used")
plt.ylabel("Average Conversion Rate")
plt.xticks(rotation=25)
plt.legend(title="Campaign Type", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "02_bar_conversion_channel_by_campaign.png"),
    bbox_inches="tight",
)
plt.close()

# 3. Box Plot: Distribution of Engagement_Score across Campaign_Type
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="Campaign_Type",
    y="Engagement_Score",
    palette="Set2",
    showmeans=True,
)
plt.title(
    "Distribution of Engagement Score Across Campaign Types",
    fontsize=13,
    pad=12,
)
plt.xlabel("Campaign Type")
plt.ylabel("Engagement Score (1-10)")
plt.savefig(
    os.path.join(OUTPUT_DIR, "03_box_engagement_by_campaign_type.png"),
    bbox_inches="tight",
)
plt.close()

# 4. Bar Chart: Average ROI by Company
plt.figure(figsize=(12, 6))
avg_roi_comp = df.groupby("Company")["ROI"].mean().sort_values(ascending=False)
sns.barplot(
    x=avg_roi_comp.index, y=avg_roi_comp.values, palette="crest", errorbar=None
)
plt.title("Average ROI by Company", fontsize=13, pad=12)
plt.xlabel("Company")
plt.ylabel("Average ROI")
plt.xticks(rotation=45)
plt.savefig(
    os.path.join(OUTPUT_DIR, "04_bar_avg_roi_by_company.png"),
    bbox_inches="tight",
)
plt.close()

# 5. Heatmap: Correlation between Engagement_Score and Conversion_Rate
plt.figure(figsize=(6, 5))
corr_matrix = df[["Engagement_Score", "Conversion_Rate"]].corr()
sns.heatmap(
    corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".3f"
)
plt.title(
    "Correlation: Engagement Score vs. Conversion Rate", fontsize=13, pad=12
)
plt.savefig(
    os.path.join(OUTPUT_DIR, "05_heatmap_engagement_vs_conversion.png"),
    bbox_inches="tight",
)
plt.close()

# 3.2 CUSTOMER SEGMENTATION
print("Generating Customer Segmentation charts...")

# 6. Count Plot: Distribution of Target_Audience
plt.figure(figsize=(10, 6))
target_order = df["Target_Audience"].value_counts().index
sns.countplot(
    data=df, x="Target_Audience", order=target_order, palette="magma"
)
plt.title("Distribution of Target Audience", fontsize=13, pad=12)
plt.xlabel("Target Audience")
plt.ylabel("Count")
plt.xticks(rotation=25)
plt.savefig(
    os.path.join(OUTPUT_DIR, "06_count_target_audience.png"),
    bbox_inches="tight",
)
plt.close()

# 7. Bar Chart: Customer_Segment with highest Conversion_Rate for each Language
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x="Language",
    y="Conversion_Rate",
    hue="Customer_Segment",
    errorbar=None,
    palette="Spectral",
)
plt.title(
    "Conversion Rate across Customer Segments by Language", fontsize=13, pad=12
)
plt.xlabel("Language")
plt.ylabel("Average Conversion Rate")
plt.legend(title="Customer Segment", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "07_bar_segment_conversion_by_language.png"),
    bbox_inches="tight",
)
plt.close()

# 8. Box Plot: Distribution of Acquisition_Cost across Customer_Segment by Channel_Used
plt.figure(figsize=(14, 7))
sns.boxplot(
    data=df,
    x="Customer_Segment",
    y="Acquisition_Cost",
    hue=channel_col,
    palette="Set3",
)
plt.title(
    f"Acquisition Cost across Customer Segments by {channel_col}",
    fontsize=13,
    pad=12,
)
plt.xlabel("Customer Segment")
plt.ylabel("Acquisition Cost ($)")
plt.xticks(rotation=25)
plt.legend(title="Channel Used", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "08_box_acquisition_by_segment_and_channel.png"),
    bbox_inches="tight",
)
plt.close()

# 9. Bar Chart: Average Conversion_Rate by Language
plt.figure(figsize=(10, 5))
avg_conv_lang = (
    df.groupby("Language")["Conversion_Rate"]
    .mean()
    .sort_values(ascending=False)
)
sns.barplot(
    x=avg_conv_lang.index,
    y=avg_conv_lang.values,
    palette="rocket",
    errorbar=None,
)
plt.title("Average Conversion Rate by Language", fontsize=13, pad=12)
plt.xlabel("Language")
plt.ylabel("Average Conversion Rate")
plt.savefig(
    os.path.join(OUTPUT_DIR, "09_bar_conversion_by_language.png"),
    bbox_inches="tight",
)
plt.close()

# 3.3 CHANNEL EFFECTIVENESS
print("Generating Channel Effectiveness charts...")

# 10. Bar Chart: Engagement_Score for Channels_Used segmented by Campaign_Type
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x=channel_col,
    y="Engagement_Score",
    hue="Campaign_Type",
    errorbar=None,
    palette="deep",
)
plt.title(
    f"Engagement Score by {channel_col} Segmented by Campaign Type",
    fontsize=13,
    pad=12,
)
plt.xlabel("Channel Used")
plt.ylabel("Average Engagement Score")
plt.xticks(rotation=25)
plt.legend(title="Campaign Type", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "10_bar_engagement_channel_by_campaign.png"),
    bbox_inches="tight",
)
plt.close()

# 11. Pie Chart: Distribution of total ROI across Channels_Used
plt.figure(figsize=(8, 8))
roi_channel = df.groupby(channel_col)["ROI"].sum()
roi_channel_positive = roi_channel[roi_channel > 0]
plt.pie(
    roi_channel_positive,
    labels=roi_channel_positive.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("pastel"),
)
plt.title(f"Distribution of Total ROI Across {channel_col}", fontsize=13, pad=12)
plt.savefig(
    os.path.join(OUTPUT_DIR, "11_pie_total_roi_by_channel.png"),
    bbox_inches="tight",
)
plt.close()

# 12. Scatter Plot: Clicks vs Impressions for each Channel_Used
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Impressions",
    y="Clicks",
    hue=channel_col,
    alpha=0.6,
    palette="Dark2",
)
plt.title(f"Clicks vs. Impressions by {channel_col}", fontsize=13, pad=12)
plt.xlabel("Impressions")
plt.ylabel("Clicks")
plt.savefig(
    os.path.join(OUTPUT_DIR, "12_scatter_clicks_vs_impressions.png"),
    bbox_inches="tight",
)
plt.close()


# 3.4 TIME-BASED ANALYSIS
print("Generating Time-Based Analysis charts...")

# 13. Histogram: Distribution of Duration
plt.figure(figsize=(10, 5))
sns.histplot(df["Duration"], kde=True, bins=25, color="teal")
plt.title("Distribution of Campaign Duration (Days)", fontsize=13, pad=12)
plt.xlabel("Duration (Days)")
plt.ylabel("Frequency")
plt.savefig(
    os.path.join(OUTPUT_DIR, "13_hist_duration.png"),
    bbox_inches="tight",
)
plt.close()

# Monthly Aggregation for clean line plots
df_valid_dates = df.dropna(subset=["Date"]).copy()
df_valid_dates["YearMonth"] = df_valid_dates["Date"].dt.to_period("M")

# 14. Line Chart: Overall Conversion_Rate change over Date for each Company
plt.figure(figsize=(14, 6))
time_comp_conv = (
    df_valid_dates.groupby(["YearMonth", "Company"])["Conversion_Rate"]
    .mean()
    .reset_index()
)
time_comp_conv["YearMonth_str"] = time_comp_conv["YearMonth"].astype(str)

sns.lineplot(
    data=time_comp_conv,
    x="YearMonth_str",
    y="Conversion_Rate",
    hue="Company",
    marker="o",
)
plt.title(
    "Monthly Average Conversion Rate Trend by Company", fontsize=13, pad=12
)
plt.xlabel("Year-Month")
plt.ylabel("Average Conversion Rate")
plt.xticks(rotation=45)
plt.legend(title="Company", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "14_line_conversion_trend_by_company.png"),
    bbox_inches="tight",
)
plt.close()

# 15. Line Chart: Trend of Engagement_Score over Date
plt.figure(figsize=(14, 5))
time_engagement = (
    df_valid_dates.groupby("YearMonth")["Engagement_Score"].mean().reset_index()
)
time_engagement["YearMonth_str"] = time_engagement["YearMonth"].astype(str)

sns.lineplot(
    data=time_engagement,
    x="YearMonth_str",
    y="Engagement_Score",
    marker="s",
    color="darkorange",
    linewidth=2.5,
)
plt.title(
    "Overall Monthly Trend of Engagement Score Over Time", fontsize=13, pad=12
)
plt.xlabel("Year-Month")
plt.ylabel("Average Engagement Score")
plt.xticks(rotation=45)
plt.savefig(
    os.path.join(OUTPUT_DIR, "15_line_engagement_score_trend.png"),
    bbox_inches="tight",
)
plt.close()

# 3.5 GEOGRAPHIC ANALYSIS
print("Generating Geographic Analysis charts...")

# 16. Bar Chart: Location with highest Acquisition_Cost
plt.figure(figsize=(12, 6))
loc_acq = (
    df.groupby("Location")["Acquisition_Cost"]
    .mean()
    .sort_values(ascending=False)
)
sns.barplot(x=loc_acq.index, y=loc_acq.values, palette="copper", errorbar=None)
plt.title("Average Acquisition Cost by Location", fontsize=13, pad=12)
plt.xlabel("Location")
plt.ylabel("Average Acquisition Cost ($)")
plt.xticks(rotation=45)
plt.savefig(
    os.path.join(OUTPUT_DIR, "16_bar_acquisition_cost_by_location.png"),
    bbox_inches="tight",
)
plt.close()

# 17. Bar Chart: Conversion_Rate by Location categorized by Target_Audience
plt.figure(figsize=(14, 7))
sns.barplot(
    data=df,
    x="Location",
    y="Conversion_Rate",
    hue="Target_Audience",
    errorbar=None,
    palette="tab10",
)
plt.title(
    "Conversion Rate across Locations by Target Audience", fontsize=13, pad=12
)
plt.xlabel("Location")
plt.ylabel("Average Conversion Rate")
plt.xticks(rotation=45)
plt.legend(title="Target Audience", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.savefig(
    os.path.join(OUTPUT_DIR, "17_bar_conversion_location_audience.png"),
    bbox_inches="tight",
)
plt.close()

# 18. Pie Chart: Proportion of ROI by Location
plt.figure(figsize=(8, 8))
roi_loc = df.groupby("Location")["ROI"].sum()
roi_loc_positive = roi_loc[roi_loc > 0]
plt.pie(
    roi_loc_positive,
    labels=roi_loc_positive.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("Set2"),
)
plt.title("Proportion of Total ROI by Location", fontsize=13, pad=12)
plt.savefig(
    os.path.join(OUTPUT_DIR, "18_pie_proportion_roi_by_location.png"),
    bbox_inches="tight",
)
plt.close()

