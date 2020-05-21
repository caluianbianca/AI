from matrixOp import transpose, multiply, inverse
from utils import myMatrix


class MyLinearMultivariateRegression:

    def __init__(self):
        self.__intercept = 0.0
        self.__coefs = []

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs

    def fit(self, inputs, outputs):

        for i in range(len(inputs)):
            inputs[i].insert(0, 1)

        X = inputs
        Y = myMatrix(outputs)

        XT = transpose(X)
        p = multiply(XT, X)
        p1 = inverse(p)
        p2 = multiply(p1, XT)
        w = multiply(p2, Y)

        self.__intercept = w[0][0]
        self.__coefs = [w[i][0] for i in range(1, len(w))]

    def predict(self, inputs):
        outputs = []
        for input in inputs:
            prediction = self.__intercept
            for pos in range(len(self.__coefs)):
                prediction += input[pos] * self.__coefs[pos]
            outputs.append(prediction)
        return outputs

    def predictionError(self, predictedOutputs, realOutputs):
        error = 0.0
        for o1, o2 in zip(predictedOutputs, realOutputs):
            error += (o1 - o2) ** 2

        return error / len(realOutputs)
