import pandas as pd
import matplotlib.pyplot as plt

# Read and combine data, ensuring Datetime is parsed as datetime
combined_df = pd.read_csv("DUQ_hourly.csv", parse_dates=["Datetime"])
combined_df.set_index("Datetime", inplace=True)

# Now the resampling should work correctly
daily_df = combined_df.resample("D").mean()

# Rest of the code remains the same

# Plot daily averages over time
plt.figure(figsize=(12, 6))
daily_df["DUQ_MW"].plot(kind="line", style="r-", label="Daily Average DUQ_MW")
plt.xlabel("Date")
plt.ylabel("Average DUQ_MW")
plt.title("Daily Average Energy Consumption")
plt.grid(True)
plt.show()
