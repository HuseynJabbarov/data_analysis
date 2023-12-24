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
# Density plot
combined_df["DUQ_MW"].plot(kind="density")
plt.title("Density of Energy Consumption Values")
plt.show()
