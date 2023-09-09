from datetime import datetime, timedelta
from delta_model import DeltaModel

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]

class DeltaCLI:
    @staticmethod
    def run():
        today = datetime.today()
        yesterday = today - timedelta(days=2)
        yesterday_str = yesterday.strftime('%Y-%m-%d')

        choice = input("Would you like the default date range (previous 30 days) or customize it? (Enter 'd' for default or 'c' for custom): ").lower()

        if choice == "d":
            start_date = (yesterday - timedelta(days=30)).strftime('%Y-%m-%d')
        elif choice == "c":
            days_ago = int(input("Enter the number of days ago to start from: "))
            start_date = (yesterday - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        else:
            print("Invalid choice!")
            exit()

        predictor = DeltaModel(start_date, yesterday_str, symbols)
        predictor.fetch_and_prepare_data()
        predictor.train_and_predict()

        predictions = predictor.get_predictions()

        for symbol in symbols:
            print(f"Predicted delta for {symbol}: {predictions[symbol]:.2f}")


if __name__ == "__main__":
    DeltaCLI.run()
