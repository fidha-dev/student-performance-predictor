import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Load dataset
df = pd.read_csv("student-por.csv")

# Select important features
df = df[["studytime", "failures", "absences", "G1", "G2", "G3"]]

# Define input and output
X = df.drop("G3", axis=1)
y = df["G3"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")