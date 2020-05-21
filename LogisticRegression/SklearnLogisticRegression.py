"""
linear_model.LogisticRegression()
- !!!transformare in k probleme binare
- atentie la outputul tool ului si cum face predictiile pe test
"""
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score


class SklearnLogisticRegression:

    def __init__(self):
        self.__classifier = LogisticRegression(multi_class='ovr')
        self.__intercept = 0
        self.__coefs = []

    def fit(self, inputs, outputs):
        self.__classifier.fit(inputs, outputs)
        self.__intercept = self.__classifier.intercept_
        self.__coefs = self.__classifier.coef_
        print("done")

    def predict(self, inputs):
        return self.__classifier.predict(inputs)

    def accuracy(self, realOutputs, predictedOutputs):
        return accuracy_score(realOutputs, predictedOutputs)

    def precision(self, realOutputs, predictedOutputs):
        return precision_score(realOutputs, predictedOutputs, average='micro')

    def recall(self, realOutputs, predictedOutputs):
        return recall_score(realOutputs, predictedOutputs, average='micro')

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs
