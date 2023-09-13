from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from delta_model import DeltaModel

app = Flask(__name__)
CORS(app)  

@app.route('/get-plot/<symbol>', methods=['GET'])
def get_plot(symbol):
    
    predictor = DeltaModel(
        (datetime.today() - timedelta(days=31)).strftime('%Y-%m-%d'), 
        (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d'), 
        [symbol]
    )
    predictor.fetch_and_prepare_data()
    predictor.train_and_predict()
    plots = predictor.plot_regression()

    plot_json = plots.get(symbol, "")
    return jsonify({"plot": plot_json})



if __name__ == "__main__":
    app.run(debug=True)