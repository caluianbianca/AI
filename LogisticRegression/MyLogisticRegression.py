'''
- gradient descent
- sigmoid
- selectare label
- testare
- metrici de performanta
- mini-batch
- !!!transformare in k probleme binare
'''
from cmath import exp
from collections import Counter
from copy import deepcopy

from MyGradientDescent import MyGradientDescent
from matrixOp import zeros_matrix, multiply, transpose, dif


class MyLogisticRegression:

    def __init__(self):
        self.__intercept = []
        self.__coefs = []

    def fit(self, x, y, learningRate=0.001, noEpochs=1000):
        labels = list(set(y))

        self.__coefs = zeros_matrix(len(labels), len(x[0]))
        self.__intercept = [0 for _ in range(len(labels))]
        for label in labels:
            X = deepcopy(x)
            currentOutputs = []
            for output in y:
                if output == label:
                    currentOutputs.append(1)
                else:
                    currentOutputs.append(0)
            gradientDescent = MyGradientDescent()
            gradientDescent.fit(X, currentOutputs)
            w0 = gradientDescent.intercept
            w = gradientDescent.coefs
            self.__intercept[label] = w0
            self.__coefs[label] = w

    def predict(self, inputs):
        predictedLabels = [self.predictOneSample(vals) for vals in inputs]
        return predictedLabels

    def predictOneSample(self, input):
        values = []
        for i in range(len(self.__intercept)):
            value = self.eval(input, self.__intercept[i], self.__coefs[i])
            values.append(value)
        maxValue = max(values)
        return values.index(maxValue)

    def sigmoid(self, x):
        return (1 / (1 + exp(-x))).real

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs

    def eval(self, input, intercept, coefs):
        output = intercept
        for j in range(len(input)):
            output += coefs[j] * input[j]
        return self.sigmoid(output)

    def accuracy(self, realOutputs, predictedOutputs):
        count = Counter(realOutputs)
        labelNames = list(set(realOutputs))
        TP = 0

        index = 0
        for label in labelNames:
            tp = 0
            for _ in range(count[label]):
                if realOutputs[index] == predictedOutputs[index]:
                    TP += 1
                    tp += 1
                index += 1
            fp = predictedOutputs.count(label) - tp
            fn = count[label] - tp

        accuracy = TP / len(realOutputs)
        return accuracy

    def precision(self, realOutputs, predictedOutputs):
        count = Counter(realOutputs)
        labelNames = list(set(realOutputs))
        TP = 0

        index = 0
        precisions = []
        recalls = []
        for label in labelNames:
            tp = 0
            for _ in range(count[label]):
                if realOutputs[index] == predictedOutputs[index]:
                    TP += 1
                    tp += 1
                index += 1
            fp = predictedOutputs.count(label) - tp
            fn = count[label] - tp
            precisions.append(tp / (tp + fp))
            recalls.append(tp / (fn + tp))

        accuracy = TP / len(realOutputs)
        return precisions

    def recall(self, realOutputs, predictedOutputs):
        count = Counter(realOutputs)
        labelNames = list(set(realOutputs))
        TP = 0

        index = 0
        precisions = []
        recalls = []
        for label in labelNames:
            tp = 0
            for _ in range(count[label]):
                if realOutputs[index] == predictedOutputs[index]:
                    TP += 1
                    tp += 1
                index += 1
            fp = predictedOutputs.count(label) - tp
            fn = count[label] - tp
            precisions.append(tp / (tp + fp))
            recalls.append(tp / (fn + tp))

        accuracy = TP / len(realOutputs)
        return recalls