from flask import Flask
from flask import request
from flask import jsonify
import pickle
import numpy as np
from math import log10

class Perceptron():
    
    def __init__(self,eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1+X.shape[1])
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                #print(xi, target)
                update = self.eta*(target-self.predict(xi))
                #print(update)
                self.w_[1:] += update*xi
                self.w_[0] += update
                #print(self.w_)
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:])+self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X)>=0.0,1,-1)


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
    
    with open("iris_model.pkl", "rb") as picklefile:
        model = pickle.load(picklefile)
    print(model)
    
    predicted_class = int(model.predict(features))
    
    return jsonify(features = features, predicted_class = predicted_class)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")