from flask import Flask, request, jsonify
import Util

app = Flask(__name__)


@app.route('/getLocationNames')
def getLocationNames():
    response = jsonify({
        'locations': Util.getLocationNames()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_price', methods=['POST'])
def predictPrice():
    location = request.form['location']
    sqmeter = float(request.form['total_sqmeter'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    response = jsonify({
        'estimated_price' : Util.getEstimatedPrice(location, sqmeter, bath, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting python Flask server for - Real Estate Market Price Prediction...')
    app.run(debug=True)
