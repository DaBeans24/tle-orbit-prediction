import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from src.tle_parser import parse_tle_file

def prepare_features(df: pd.DataFrame):
    features = ["inclo", "eccentricity", "raan", "argpo", "mean_anomaly", "mean_motion"]
    df = df.sort_values("epoch")
    X = df[features].iloc[:-1]
    y = df[features].shift(-1).dropna()
    return X, y, features

def predict_next_orbit(tle_file: str):
    # Parse TLE data
    df = parse_tle_file(tle_file)
    if df.empty or len(df) < 2:
        print("[✖] Not enough data to predict.")
        return

    # Prepare training data
    X, y, feature_names = prepare_features(df)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Predict next timestep
    next_input = scaler.transform([X.iloc[-1]])
    next_prediction = model.predict(next_input)[0]

    # Print results
    print("\n📈 Predicted orbital elements for next timestep:")
    for name, value in zip(feature_names, next_prediction):
        print(f"  {name:<15}: {value:.6f}")

if __name__ == "__main__":
    predict_next_orbit("data/starlink.txt")
