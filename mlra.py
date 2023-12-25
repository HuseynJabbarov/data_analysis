import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('boston.csv')  # replace with your file path

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print("\nMissing values in each column:\n", data.isnull().sum())

# Explore data statistics
print("\nData Statistics:\n", data.describe())

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()

# Splitting the data into training and test sets
X = data.drop('MEDV', axis=1)  # Features
y = data['MEDV']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Displaying coefficients in a bar plot
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
coefficients = coefficients.sort_values(by='Coefficient', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients['Coefficient'], y=coefficients.index)
plt.title('Coefficients in the Linear Regression Model')
plt.xlabel('Coefficient Value')
plt.ylabel('Features')
plt.show()
