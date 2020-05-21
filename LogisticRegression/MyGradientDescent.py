from copy import deepcopy

from numpy import random, exp

from utils import copy_matrix


class MyGradientDescent:

    def __init__(self):
        self.__intercept = 0.0
        self.__coefs = []

    @property
    def intercept(self):
        return self.__intercept

    @property
    def coefs(self):
        return self.__coefs

    def fit(self, inputs, outputs, learningRate=0.001, noEpochs=1000):
        self.__coefs = [0.0 for _ in range(len(inputs[0]) + 1)]
        inputsCopy = deepcopy(inputs)
        outputsCopy = deepcopy(outputs)
        for epoch in range(noEpochs):
            inputs = deepcopy(inputsCopy)
            outputs = deepcopy(outputsCopy)
            mini_batches = self.create_mini_batches(inputs, outputs, len(inputs) // 10)
            for batch in mini_batches:
                crtInputs = [batch[i][0] for i in range(len(batch))]
                crtOutputs = [batch[i][1] for i in range(len(batch))]
                crtError = 0.0
                i = 0
                for i in range(len(batch)):
                    ycomputed = self.sigmoid(self.eval(crtInputs[i]))
                    crtError += ycomputed - crtOutputs[i]
                j = 0
                for j in range(0, len(self.__coefs) - 1):
                    self.__coefs[j] = self.__coefs[j] - learningRate * crtError * crtInputs[i][j]
                self.__coefs[j+1] = self.__coefs[j+1] - learningRate * crtError * 1

        self.__intercept = self.__coefs[-1]
        self.__coefs = self.__coefs[:-1]

    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def eval(self, input):
        output = self.__coefs[-1]
        for j in range(len(input)):
            output += self.__coefs[j] * input[j]
        return output

    def predict(self, inputs):
        outputs = [self.eval(input) for input in inputs]
        return outputs

    def predictionError(self, predictedOutputs, realOutputs):
        error = 0.0
        for o1, o2 in zip(predictedOutputs, realOutputs):
            error += (o1 - o2) ** 2

        return error / len(realOutputs)

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
            for j in range(batch_size - 1):
                i += 1
                batch.append((data[i][:-1], data[i][len(data[i]) - 1]))
            mini_batches.append(batch)

        if i != len(inputs):
            batch = []
            for j in range(len(inputs) - i - 1):
                i += 1
                batch.append((data[i][:-1], data[i][len(data[i]) - 1]))
            mini_batches.append(batch)

        return mini_batches
