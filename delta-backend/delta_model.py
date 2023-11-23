import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import mpld3
import matplotlib
import base64
import io
import plotly.graph_objects as go

matplotlib.use('Agg')


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
        plots = {}
        accuracies = {}
        for symbol in self.symbols:
            stock_data = self.training_data[symbol]

            # We'll use all data except the last row (last day) as training data
            X_train = stock_data.iloc[:-1][["Open", "High", "Low", "Volume"]]
            y_train = stock_data.iloc[:-1]["delta"]
            
            # Training the model
            model = LinearRegression().fit(X_train, y_train)

            # Predict using the trained model
            predicted_deltas = model.predict(X_train)

            # Calculate R-squared
            r_squared = r2_score(y_train, predicted_deltas)
            accuracies[symbol] = r_squared

            # Plotting
            plt.figure(figsize=(12, 6))
            plt.plot(stock_data.index[:-1], y_train, label='True', color='blue')
            plt.plot(stock_data.index[:-1], predicted_deltas, label='Predicted', linestyle='--', color='red')
            plt.xlabel("Date")
            plt.ylabel("Delta")
            plt.legend()
            plt.grid(True)
           
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(x=stock_data.index[:-1], y=y_train, mode='lines', name='True'))
            fig.add_trace(go.Scatter(x=stock_data.index[:-1], y=predicted_deltas, mode='lines', name='Predicted', line=dict(dash='dash')))
            
            fig.update_layout(height=800) 
            fig.update_layout(font_color="white")
            fig.update_layout(title=f"Regression for {symbol} (R-squared: {r_squared:.4f})")

            # Convert Plotly plot to JSON
            plots[symbol] = fig.to_json()

          
        return plots 