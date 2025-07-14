import pandas as pd
from sklearn.preprocessing import StandardScaler

def prepare_dataset(df):
    df = df.sort_values("epoch")
    features = ["inclo", "eccentricity", "raan", "argpo", "mean_anomaly", "mean_motion"]
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    y = df[features].shift(-1).dropna().values  # Predict next state
    X = X[:-1]
    return X, y, scaler

