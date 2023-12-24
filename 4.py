import pandas as pd
import matplotlib.pyplot as plt

# Read and combine data
combined_df = pd.read_csv("DUQ_hourly.csv", parse_dates=["Datetime"])
combined_df.set_index("Datetime", inplace=True)

# Calculate rolling averages and standard deviations
rolling_mean = combined_df["DUQ_MW"].rolling(window=24).mean()
rolling_std = combined_df["DUQ_MW"].rolling(window=24).std()

# Plot rolling statistics
plt.figure(figsize=(12, 6))
plt.plot(combined_df.index, rolling_mean, label="Rolling Average")
plt.plot(combined_df.index, rolling_std, label="Rolling Standard Deviation")
plt.xlabel("Datetime")
plt.ylabel("DUQ_MW")
plt.legend()
plt.show()

# Further analysis (optional)
# ... Compare rolling stats across different time windows
# ... Analyze periods with high/low deviations

