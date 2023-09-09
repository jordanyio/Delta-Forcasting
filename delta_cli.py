from datetime import datetime, timedelta
from delta_model import DeltaModel

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]

class DeltaCLI:
    @staticmethod
    def run():
        today = datetime.today()
        yesterday = today - timedelta(days=1)
        yesterday_str = yesterday.strftime('%Y-%m-%d')

        choice = input("Would you like the default date range (previous 30 days) or customize it? (Enter 'd' for default or 'c' for custom): ").lower()

        if choice == "d":
            start_date = (yesterday - timedelta(days=30)).strftime('%Y-%m-%d')
            print("----------------")
            print("Your start date is: " + start_date)
            print("----------------")
        elif choice == "c":
            print("----------------")
            print("Attention !")
            print("----------------")
            print("If your start and end date do not land on a trading day, the dates will automatically be set to the last trading day prior to your end date for the end date, and the first trading day that occurred after the start date.")
            print("----------------")
            days_ago = int(input("Enter the number of days ago to start from: "))
            start_date = (yesterday - timedelta(days=days_ago)).strftime('%Y-%m-%d')
            print("----------------")
            print("Your start date is: " + start_date)
            print("----------------")
            shift_choice = input("Do you want to shift the last day? Default is last trading day. Enter (y/n): ").lower()

            if shift_choice == 'y':
                shift_days = int(input("Enter the number of days to shift the last day by: "))
                yesterday_str = (today - timedelta(days=shift_days)).strftime('%Y-%m-%d')
                print("----------------")
                print("Your end date is: " + yesterday_str)
                print("----------------")
            else:
                print("----------------")
                print("Your end date is: " + yesterday_str)
                print("----------------")

        else:
            print("Invalid choice!")
            exit()

        predictor = DeltaModel(start_date, yesterday_str, symbols)
        predictor.fetch_and_prepare_data()
        predictor.train_and_predict()
        predictor.plot_regression()

        predictions = predictor.get_predictions()

        for symbol in symbols:
            print(f"Predicted delta for {symbol}: {predictions[symbol]:.2f}")


if __name__ == "__main__":
    DeltaCLI.run()
