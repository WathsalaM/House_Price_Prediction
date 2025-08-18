import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic dataset
np.random.seed(42)
n_samples = 500

square_feet = np.random.randint(500, 4000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples)
age = np.random.randint(0, 50, n_samples)

# Price formula (just for simulation)
price = (square_feet * 200) + (bedrooms * 10000) + (bathrooms * 5000) - (age * 300) + np.random.randint(-20000, 20000, n_samples)

# Create DataFrame
df = pd.DataFrame({
    "square_feet": square_feet,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "age": age,
    "price": price
})

# Split data
X = df[["square_feet", "bedrooms", "bathrooms", "age"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Test MSE: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Save model + metadata
joblib.dump({
    "model": model,
    "features": X.columns.tolist(),
    "mse": mse,
    "r2": r2
}, "model.pkl")

print("✅ Model saved as model.pkl")
