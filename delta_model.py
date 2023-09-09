import yfinance as yf
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class DeltaModel:
    def __init__(self, start_date, end_date, symbols):
        self.start_date = start_date
        self.end_date = end_date
        self.symbols = symbols
        self.training_data = {}
        self.predicted_delta = {}

    def fetch_and_prepare_data(self):
        for symbol in self.symbols:
            stock_data = yf.download(symbol, start=self.start_date, end=self.end_date)
            stock_data["delta"] = stock_data["Close"].diff()
            stock_data = stock_data.dropna()  # Drop the first row because the diff() will create a NaN value for the first row
            self.training_data[symbol] = stock_data

    def train_and_predict(self):
        for symbol in self.symbols:
            stock_data = self.training_data[symbol]

            # We'll use all data except the last row (last day) as training data
            X_train = stock_data.iloc[:-1][["Open", "High", "Low", "Volume"]]
            y_train = stock_data.iloc[:-1]["delta"]

            model = LinearRegression().fit(X_train, y_train)

            # The last row (last day) will be used for prediction
            X_pred = stock_data.iloc[-1:][["Open", "High", "Low", "Volume"]]
            delta_pred = model.predict(X_pred)[0]

            self.predicted_delta[symbol] = delta_pred

    def get_predictions(self):
        return self.predicted_delta

    def plot_regression(self):
        for symbol in self.symbols:
            stock_data = self.training_data[symbol]

            # We'll use all data except the last row (last day) as training data
            X_train = stock_data.iloc[:-1][["Open", "High", "Low", "Volume"]]
            y_train = stock_data.iloc[:-1]["delta"]
            
            # Training the model
            model = LinearRegression().fit(X_train, y_train)

            # Predict using the trained model
            predicted_deltas = model.predict(X_train)

            # Plotting
            plt.figure(figsize=(12, 6))
            plt.plot(stock_data.index[:-1], y_train, label='True Deltas', color='blue')
            plt.plot(stock_data.index[:-1], predicted_deltas, label='Predicted Deltas', linestyle='--', color='red')
            plt.title(f"Regression for {symbol}")
            plt.xlabel("Date")
            plt.ylabel("Delta")
            plt.legend()
            plt.grid(True)
            plt.show()

