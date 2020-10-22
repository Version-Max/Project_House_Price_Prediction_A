from flask import Flask, request, jsonify
import utilities
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# -- CORS
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
# -- CORS

app = Flask(__name__)


# Get location names
@app.route('/location_names', methods=['GET'])
def location_names():
    # Getting locations from utilities.py server
    location = jsonify({
        'location': utilities.location_names()
    })
    location.headers.add('Access-Control-Allow-Origin', '*')

    return location


@app.route('/predict_home_price', methods=['GET', 'OPTIONS'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    lcn = request.form['lcn']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    response = jsonify({
        'estimated_price': utilities.Price_Predict(location, total_sqft, bath, bed)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Get input of Bed, Baths, Location, SqFt to predict the price:
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    bed = request.form['Bed']
    Bad = request.form['Bad']
    response = jsonify({
        'beds': utilities.ask(bed, Bad)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print('Server side print', response)
    return response


''' Dummy function: START --- [Works for Sure]
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    bed = request.form['Bed']
    Bad = request.form['Bad']
    response = jsonify({
        'beds': utilities.ask(bed, Bad)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print('Server side print', response)
    return response
# Dummy END --- '''


@app.route('/price_predict', methods=['GET', 'POST'])
def price_predict():
    bed = request.form['bed']
    sqft = request.form['sqft']
    bath = request.form['bath']
    lcn = request.form['lcn']
    print('\n\n[1] Server func Price-Predict invoked.')
    print(bed)
    print(bath)
    print(sqft)
    print(lcn)
    response = ({
        'price': utilities.Price_Predict(lcn, sqft, bath, bed)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    print('\n\nServer side print', response)
    jake = response['price']
    print('Response.Price is: ')
    print(jake)

    responsea = jsonify({
       # 'beds': utilities.ask(Belt=1, Bad=5)
        'beds' : utilities.Price_Predict(lcn, sqft, bath, bed)
    })
    responsea.headers.add('Access-Control-Allow-Origin', '*')
    print('Server side print', responsea)
    return responsea


if __name__ == "__main__":
    print('Starting Python flask server')
    utilities.load__model_and_column_names()
    app.run()
