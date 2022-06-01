import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(data = np.c_[iris["data"], iris["target"]], columns = iris["feature_names"]+["target"])
df.drop(df.index[df["target"] == 2], inplace = True)
X = df.loc[:, ["petal length (cm)", "sepal length (cm)"]].values
Y = df.loc[:, ["target"]].values

class Perceptron():
    
    def __init__(self,eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, Y):
        self.w_ = np.zeros(1+X.shape[1])
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,Y):
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

model = Perceptron()
model.fit(X,Y)

with open("iris.pkl", "wb") as this_model:
    pickle.dump(model, this_model)