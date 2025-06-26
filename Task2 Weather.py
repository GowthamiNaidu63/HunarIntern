# 1. Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 2. Load historical weather data
# Replace the URL or path with your actual CSV file
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
df = pd.read_csv(url)

# Rename column if necessary and simulate additional weather features for demo purposes
df.rename(columns={'Temp': 'Temperature'}, inplace=True)
np.random.seed(42)
df['Humidity'] = np.random.uniform(30, 90, len(df))
df['WindSpeed'] = np.random.uniform(5, 30, len(df))

# 3. Data Cleaning - remove nulls and duplicates
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# 4. Select Features and Target
X = df[['Humidity', 'WindSpeed']]
y = df['Temperature']

# 5. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 6. Apply Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score (Accuracy):", r2)

# 8. Plot predictions vs actual
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
plt.xlabel("Actual Temperature")
plt.ylabel("Predicted Temperature")
plt.title("Actual vs Predicted Temperature")
plt.grid(True)
plt.show()

# 9. Test model on different data
sample_data = pd.DataFrame({
    'Humidity': [50, 70, 85],
    'WindSpeed': [10, 15, 20]
})
sample_prediction = model.predict(sample_data)
print("\nTest Predictions for New Data:\n", sample_prediction)
