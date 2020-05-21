import random

from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error


class SklearnBGD:

    def __init__(self):
        self.__intercept = 0.0
        self.__coefs = []
        self.__regressor = None

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs

    def fit(self, inputs, outputs, learningRate=0.001, noEpochs=1000):
        regressor = SGDRegressor(max_iter=noEpochs, eta0=learningRate, shuffle=True)
        self.__regressor = regressor
        miniBatches = self.create_mini_batches(inputs, outputs, len(inputs) // 10)
        for batch in miniBatches:
            crtInputs = [batch[i][0] for i in range(len(batch))]
            crtOutputs = [batch[i][1] for i in range(len(batch))]
            self.__regressor.partial_fit(crtInputs, crtOutputs)
        self.__intercept = self.__regressor.intercept_
        self.__coefs = self.__regressor.coef_

    def eval(self, input):
        return

    def predict(self, inputs):
        return self.__regressor.predict(inputs)

    def predictionError(self, predictedOutputs, realOutputs):
        return mean_squared_error(realOutputs, predictedOutputs)

    def create_mini_batches(self, inputs, outputs, batch_size):
        mini_batches = []
        data = []
        for pos in range(len(inputs)):
            line = inputs[pos]
            line.append(outputs[pos])
            data.append(line)
        random.shuffle(data)

        noBatches = len(inputs) // batch_size

        i = 0
        for _ in range(noBatches):
            batch = []
            for j in range(batch_size):
                i += 1
                batch.append((data[i][:-1], data[i][len(data[i]) - 1]))
            mini_batches.append(batch)

        if len(inputs) % batch_size != 0:
            batch = []
            for j in range(len(inputs) - i - 1):
                i += 1
                batch.append((data[i][:-1], data[i][len(data[i]) - 1]))
            mini_batches.append(batch)

        return mini_batches