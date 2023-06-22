import yfinance as yf
from sklearn.linear_model import LinearRegression

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]

training_data = {}

for symbol in symbols:
    stock_data = yf.download(symbol, start="2015-01-01", end="2022-03-20")
    stock_data["delta"] = stock_data["Close"].diff()
    stock_data = stock_data.iloc[1:]
    training_data[symbol] = stock_data

predicted_delta = {}

for symbol in symbols:
    stock_data = training_data[symbol]
    X = stock_data[["Open", "High", "Low", "Volume"]]
    y = stock_data["delta"]
    model = LinearRegression().fit(X, y)
    latest_data = yf.download(symbol, start="2022-03-21", end="2022-03-21")
    X_pred = latest_data[["Open", "High", "Low", "Volume"]]
    delta_pred = model.predict(X_pred)[0]
    predicted_delta[symbol] = delta_pred

for symbol in symbols:
    print(f"Predicted delta for {symbol}: {predicted_delta[symbol]:.2f}")
