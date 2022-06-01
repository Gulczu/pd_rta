from flask import Flask
from flask import request
from flask import jsonify
import pickle
import perc

app = Flask(__name__)

@app.route('/home')
def hello():
    print("Hello World")

@app.route('/api/predict', methods = ["GET"])
def get_prediction():
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))
    features = [sepal_length, petal_length]
    print(features)
    
    with open("iris.pkl", "rb") as picklefile:
        model = pickle.load(picklefile)
    print(model)
    
    predicted_class = int(model.predict(features))
    
    return jsonify(features = features, predicted_class = predicted_class)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")