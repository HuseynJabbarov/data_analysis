import pandas as pd
import matplotlib.pyplot as plt

# Define file paths
file_paths = ["DUQ_hourly.csv"]

# Read and combine data
combined_df = pd.DataFrame()
for file_path in file_paths:
    df = pd.read_csv(file_path)
    df.set_index("Datetime", inplace=True)
    combined_df = pd.concat([combined_df, df])  # Use pd.concat() for concatenation

# Rest of the code remains the same

# Plot time series data
plt.figure(figsize=(12, 6))
combined_df["DUQ_MW"].plot(kind="line", style="r-", label="DUQ_MW")
plt.xlabel("Datetime")
plt.ylabel("DUQ_MW")
plt.title("Hourly Energy Consumption")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.grid(True)
plt.show()

# Optional exploration steps
# ...
