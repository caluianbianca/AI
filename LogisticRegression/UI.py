'''
- plot rezultate, forma output
'''
from matplotlib import pyplot as plt

from MyLogisticRegression import MyLogisticRegression


class UI:

    def __init__(self, data, logisticRegression):
        self.__data = data
        self.__logisticRegression = logisticRegression

    def run(self):
        self.plotDistribution()
        self.plotHistograms()
        self.plotNormalisedTrainData()

        sumAccuracy = 0
        bestLr = None
        bestAcc = 0
        for pos in range(len(self.__data.folds)):
            testInput = [self.__data.inputs[self.__data.folds[pos][pos]]]
            testOutput = [self.__data.outputs[self.__data.folds[pos][pos]]]
            trainInputs = []
            trainOutputs = []
            for foldPos in range(len(self.__data.folds[pos])):
                if foldPos != pos:
                    trainInputs.append(self.__data.inputs[self.__data.folds[pos][foldPos]])
                    trainOutputs.append(self.__data.outputs[self.__data.folds[pos][foldPos]])
            newLr = MyLogisticRegression()
            newLr.fit(trainInputs, trainOutputs)
            predictedOutputs = newLr.predict(testInput)
            currentAccuracy = newLr.accuracy(testOutput, predictedOutputs)
            sumAccuracy += currentAccuracy
            if currentAccuracy > bestAcc:
                bestAcc = currentAccuracy
                bestLr = newLr

        maccuracy = sumAccuracy / len(self.__data.folds)
        print("kfolds acc: ", maccuracy)
        lr = bestLr
        lr.fit(self.__data.inputs, self.__data.outputs)
        #self.__logisticRegression.fit(self.__data.trainInput, self.__data.trainOutput)
        w0 = lr.intercept
        print("w0 = " + str(w0))
        print("w = " + str(lr.coefs))

        '''predictedOutputs = lr.predict(self.__data.testInput)
        accuracy = self.__logisticRegression.accuracy(self.__data.testOutput, predictedOutputs)
        precision = self.__logisticRegression.precision(self.__data.testOutput, predictedOutputs)
        recall = self.__logisticRegression.recall(self.__data.testOutput, predictedOutputs)
'''
        #("accuracy = " + str(accuracy))
        #print("precision = " + str(precision))
        #print("recall = " + str(recall))


    def plotDistribution(self):
        virginica = [self.__data.inputs[i] for i in range(len(self.__data.inputs)) if self.__data.outputs[i] == 2]
        versicolor = [self.__data.inputs[i] for i in range(len(self.__data.inputs)) if self.__data.outputs[i] == 1]
        setosa = [self.__data.inputs[i] for i in range(len(self.__data.inputs)) if self.__data.outputs[i] == 0]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = [feat[0] for feat in virginica]
        y = [feat[1] for feat in virginica]
        z = [feat[2] for feat in virginica]
        c = [feat[3] for feat in virginica]

        ax.scatter(x, y, z, c=c, marker='o', cmap=plt.hot())

        x = [feat[0] for feat in versicolor]
        y = [feat[1] for feat in versicolor]
        z = [feat[2] for feat in versicolor]
        c = [feat[3] for feat in versicolor]

        ax.scatter(x, y, z, c=c, marker='_', cmap=plt.hot())

        x = [feat[0] for feat in setosa]
        y = [feat[1] for feat in setosa]
        z = [feat[2] for feat in setosa]
        c = [feat[3] for feat in setosa]

        ax.scatter(x, y, z, c=c, marker='^', cmap=plt.hot())
        plt.title("data")
        plt.show()

    def plotHistogram(self, feat, name):
        n, bins, patches = plt.hist(feat, 10)
        plt.title(name)
        plt.show()

    def plotHistograms(self):
        f1 = [feature[0] for feature in self.__data.inputs]
        f2 = [feature[1] for feature in self.__data.inputs]
        f3 = [feature[2] for feature in self.__data.inputs]
        f4 = [feature[3] for feature in self.__data.inputs]

        self.plotHistogram(f1, "sepal length in cm")
        self.plotHistogram(f2, "sepal width in cm")
        self.plotHistogram(f3, "petal length in cm")
        self.plotHistogram(f4, "petal width in cm")

    def plotNormalisedTrainData(self):
        virginica = [self.__data.inputs[i] for i in range(len(self.__data.trainInput)) if
                     self.__data.outputs[i] == 0]
        versicolor = [self.__data.inputs[i] for i in range(len(self.__data.trainInput)) if
                      self.__data.outputs[i] == 1]
        setosa = [self.__data.inputs[i] for i in range(len(self.__data.trainInput)) if
                  self.__data.outputs[i] == 2]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = [feat[0] for feat in virginica]
        y = [feat[1] for feat in virginica]
        z = [feat[2] for feat in virginica]
        c = [feat[3] for feat in virginica]

        ax.scatter(x, y, z, c=c, marker='o', cmap=plt.hot())

        x = [feat[0] for feat in versicolor]
        y = [feat[1] for feat in versicolor]
        z = [feat[2] for feat in versicolor]
        c = [feat[3] for feat in versicolor]

        ax.scatter(x, y, z, c=c, marker='_', cmap=plt.hot())

        x = [feat[0] for feat in setosa]
        y = [feat[1] for feat in setosa]
        z = [feat[2] for feat in setosa]
        c = [feat[3] for feat in setosa]

        ax.scatter(x, y, z, c=c, marker='^', cmap=plt.hot())
        plt.title("normalised train data")
        plt.show()
