from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    print(f"MSE: {mse:.6f}")
    return model, preds

