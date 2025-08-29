import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# File paths
dataset_path = "austin_weather_clean.csv"
model_path = "rainfall_model.pkl"
scaler_path = "scaler.pkl"

try:
    # Check if dataset exists
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Select relevant features and target
    features = [
        "TempHighF", "TempAvgF", "TempLowF", "DewPointHighF", "DewPointAvgF", "DewPointLowF",
        "HumidityHighPercent", "HumidityAvgPercent", "HumidityLowPercent", "SeaLevelPressureAvgInches",
        "VisibilityHighMiles", "VisibilityAvgMiles", "VisibilityLowMiles", "WindHighMPH", "WindAvgMPH", "WindGustMPH"
    ]
    target = "PrecipitationSumInches"

    # Check if required columns exist
    missing_columns = [col for col in features + [target] if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in dataset: {missing_columns}")

    # Drop rows with missing values
    df = df.dropna(subset=features + [target])

    # Split data
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train Random Forest Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model & scaler
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    print("✅ Model training complete and saved!")

except FileNotFoundError as e:
    print(f"❌ Error: {e}")
except ValueError as e:
    print(f"❌ Error: {e}")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

# Add a function to load the model and scaler for API integration
def load_model_and_scaler():
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except Exception as e:
        print(f"❌ Error loading model or scaler: {e}")
        return None, None