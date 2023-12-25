import pandas as pd
import matplotlib.pyplot as plt

# Read and combine data
combined_df = pd.read_csv("DUQ_hourly.csv", parse_dates=["Datetime"])
combined_df.set_index("Datetime", inplace=True)

# Calculate daily, weekly, and monthly averages
daily_df = combined_df.resample("D").mean()
weekly_df = combined_df.resample("W").mean()
monthly_df = combined_df.resample("M").mean()

# Create subplots
fig, (ax2, ax3) = plt.subplots(2, 1, figsize=(12, 10))

# Plot weekly averages
weekly_df["DUQ_MW"].plot(ax=ax2, style="g-", label="Weekly Average")
ax2.set_title("Weekly Average Energy Consumption")

# Plot monthly averages
monthly_df["DUQ_MW"].plot(ax=ax3, style="b-", label="Monthly Average")
ax3.set_title("Monthly Average Energy Consumption")

plt.show()
