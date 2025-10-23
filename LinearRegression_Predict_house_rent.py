# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Sample house rent dataset
data = {
    'area_sqft': [1000, 1500, 1200, 1800, 2000, 1100, 1600, 1300, 1700, 1400],
    'bedrooms': [2, 3, 2, 4, 3, 2, 3, 2, 4, 3],
    'age': [5, 10, 3, 8, 12, 2, 6, 4, 7, 5],
    'rent': [25000, 40000, 30000, 45000, 50000, 27000, 42000, 32000, 46000, 38000]
}
df = pd.DataFrame(data)

# Step 2: Split dataset into features (X) and target (y)
X = df[['area_sqft', 'bedrooms', 'age']]  # independent variables
y = df['rent']                             # dependent variable

# Step 3: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict rent
y_pred = model.predict(X_test)

# Step 6: Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
# rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print("Predicted Rent:", y_pred)
print("MAE:", mae)
print("MSE:", mse)
# print("RMSE:", rmse)
print("R² Score:", r2)
