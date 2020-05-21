'''
iris setos, iris versicolor, iris verginica
- lungime si latime sepala, lungime si latime petala
- impartire train/test = 80/20
- normalizarea datelor
'''
import csv

import numpy


class Data:

    def __init__(self, filename):
        self.__filename = filename
        self.__inputs, self.__outputs = self.loadData()
        self.__trainInput = []
        self.__trainOutput = []
        self.__testInput = []
        self.__testOutput = []
        self.__folds = []
        self.transformLabels()
        self.kFolds()
        self.splitData()
        self.inputsStandardisation()

    @property
    def trainInput(self):
        return self.__trainInput

    @property
    def trainOutput(self):
        return self.__trainOutput

    @property
    def testInput(self):
        return self.__testInput

    @property
    def testOutput(self):
        return self.__testOutput

    @property
    def folds(self):
        return self.__folds

    @property
    def inputs(self):
        return self.__inputs

    @property
    def outputs(self):
        return self.__outputs

    def loadData(self):
        inputs = []
        outputs = []
        with open(self.__filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row != []:
                    inputs.append(list(map(float, row[:4])))
                    outputs.append(row[len(row) - 1])
        return inputs, outputs

    def splitData(self):
        numpy.random.seed(5)
        indexes = [i for i in range(len(self.__inputs))]
        trainSample = numpy.random.choice(indexes, int(0.8 * len(self.__inputs)), replace=False)
        testSample = [i for i in indexes if not i in trainSample]

        self.__trainInput = [self.__inputs[i] for i in trainSample]
        self.__trainOutput = [self.__outputs[i] for i in trainSample]

        self.__testInput = [self.__inputs[i] for i in testSample]
        self.__testOutput = [self.__outputs[i] for i in testSample]

    def kFolds(self, k=5):
        numpy.random.seed(5)
        indexes = [i for i in range(len(self.__inputs))]
        indexesRandom = numpy.random.choice(indexes, int(len(self.__inputs)), replace=False)
        folds = []
        foldSize = len(self.__inputs) // k

        i = 0
        for _ in range(k - 1):
            fold = []
            for j in range(foldSize - 1):
                i += 1
                fold.append(indexesRandom[i])
            folds.append(fold)

        if i != len(indexesRandom):
            fold = []
            for j in range(len(indexesRandom) - i -1):
                i += 1
                fold.append(indexesRandom[i])
            folds.append(fold)
        self.__folds = folds

    def standardisation(self, data, meanValue=None, stDev=None):
        if meanValue is None and stDev is None:
            meanValue = sum(data) / len(data)
            stDev = (1 / len(data) * sum([(d - meanValue) ** 2 for d in data])) ** 0.5
        zScore = [(d - meanValue) / stDev for d in data]
        return zScore, meanValue, stDev

    def inputsStandardisation(self):
        sepalLength = [features[0] for features in self.__inputs]
        sepalWidth = [features[1] for features in self.__inputs]
        petalLength = [features[2] for features in self.__inputs]
        petalWidth = [features[3] for features in self.__inputs]

        sepalLength, meanValueSepalLength, stDevSepalLength = self.standardisation(sepalLength)
        sepalWidth, meanValueSepalWidth, stDevSepalWidth = self.standardisation(sepalWidth)
        petalLength, meanValuePetalLength, stDevPetalLength = self.standardisation(petalLength)
        petalWidth, meanValuePetalWidth, stDevPetalWidth = self.standardisation(petalWidth)

        self.__inputs = [[sepalLength[i], sepalWidth[i], petalLength[i], petalWidth[i]]
                             for i in range(len(sepalWidth))]

    def transformLabels(self):
        labels = list(set(self.__outputs))
        for pos in range(len(self.__outputs)):
            self.__outputs[pos] = labels.index(self.__outputs[pos])
