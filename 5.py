import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.holtwinters import Holt
from scipy.stats import zscore  # Corrected import path

# Read and combine data
combined_df = pd.read_csv("DUQ_hourly.csv", parse_dates=["Datetime"])
combined_df.set_index("Datetime", inplace=True)

# Fit a Holt model with trend
model = Holt(combined_df["DUQ_MW"]).fit()

# Calculate z-scores for residuals
zscores = zscore(combined_df["DUQ_MW"] - model.fittedvalues)

# Identify potential anomalies based on z-scores (customize thresholds as needed)
threshold = 10  # Adjust as appropriate for your data
anomalies = combined_df[zscores > threshold]

# Print or visualize anomalies
print("Potential anomalies:")
print(anomalies)

# Consider visualizing anomalies on a time series plot
plt.figure(figsize=(12, 6))  # Adjust figure size as needed
combined_df["DUQ_MW"].plot(label="Original Data")
anomalies["DUQ_MW"].plot(style="o", color="red", label="Anomalies")
plt.legend()
plt.xlabel("Datetime")
plt.ylabel("DUQ_MW")
plt.title("Energy Consumption with Anomalies")
plt.show()