from copy import deepcopy

import matplotlib.pyplot as plt

class UI:

    def __init__(self, data, regression):
        self.__data = data
        self.__regression = regression

    def run(self):
        self.plotHistograms(self.__data.inputs, self.__data.outputs)
        self.plotLiniarity(self.__data.inputs, self.__data.outputs)
        self.__regression.fit(deepcopy(self.__data.trainInputs), deepcopy(self.__data.trainOutputs))
        w0 = self.__regression.intercept
        w = self.__regression.coefs
        print("w0 = " + str(w0))
        print("w = " + str(w))

        self.plotTrainVsTest(self.__data.trainInputs, self.__data.testInputs, self.__data.trainOutputs, self.__data.testOutputs)

        predictions = self.__regression.predict(self.__data.testInputs)
        error = self.__regression.predictionError(predictions, self.__data.testOutputs)
        print("error = " + str(error))

        self.plotModel(self.__data.trainInputs, self.__data.trainOutputs)

    def plotModel(self, inputs, outputs):
        gdpInputs = [values[0] for values in inputs]
        freedomInputs = [values[1] for values in inputs]

        w0, w1, w2 = self.__regression.intercept, self.__regression.coefs[0], self.__regression.coefs[1]
        noOfPoints = 50

        xref1 = []
        val = min(gdpInputs)
        step1 = (max(gdpInputs) - min(gdpInputs)) / noOfPoints
        for _ in range(1, noOfPoints):
            for _ in range(1, noOfPoints):
                xref1.append(val)
            val += step1

        xref2 = []
        val = min(freedomInputs)
        step2 = (max(freedomInputs) - min(freedomInputs)) / noOfPoints
        for _ in range(1, noOfPoints):
            aux = val
            for _ in range(1, noOfPoints):
                xref2.append(aux)
                aux += step2

        yref = [w0 + w1 * el1 + w2 * el2 for el1, el2 in zip(xref1, xref2)]
        self.plot3Ddata(gdpInputs, freedomInputs, outputs, xref1, xref2, yref, [], [], [],
                        'train data and learnt model')

    def plot3Ddata(self, x1Train, x2Train, yTrain, x1Model=None, x2Model=None, yModel=None, x1Test=None, x2Test=None,
                   yTest=None, title=None):
        ax = plt.axes(projection='3d')
        if x1Train:
            plt.scatter(x1Train, x2Train, yTrain, c='r', marker='o', label='train data')
        if x1Model:
            plt.scatter(x1Model, x2Model, yModel, c='b', marker='_', label='learnt model')
        if x1Test:
            plt.scatter(x1Test, x2Test, yTest, c='g', marker='^', label='test data')
        plt.title(title)
        ax.set_xlabel("capita")
        ax.set_ylabel("freedom")
        ax.set_zlabel("happiness")
        plt.legend()
        plt.show()

    def plotLiniarity(self, inputs, outputs):
        gdpInputs = [values[0] for values in inputs]
        freedomInputs = [values[1] for values in inputs]
        outputs = [value for value in outputs]
        self.plot3Ddata(gdpInputs, freedomInputs, outputs, [], [], [], [], [], [], 'capita vs freedom vs happiness')

    def plotHistograms(self, inputs, outputs):
        gdpInputs = [values[0] for values in inputs]

        freedomInputs = [values[1] for values in inputs]

        n, bins, patches = plt.hist(gdpInputs, 10)
        plt.title("Histogram of GDP capita")
        plt.show()

        n, bins, patches = plt.hist(freedomInputs, 10)
        plt.title("Histogram of freedom")
        plt.show()

        n, bins, patches = plt.hist(outputs, 10)
        plt.title("Histogram of happiness")
        plt.show()

    def plotTrainVsTest(self, trainInputs, testInputs, trainOutputs, testOutputs):
        feature1train = [ex[0] for ex in trainInputs]
        feature2train = [ex[1] for ex in trainInputs]

        feature1test = [ex[0] for ex in testInputs]
        feature2test = [ex[1] for ex in testInputs]

        self.plot3Ddata(feature1train, feature2train, trainOutputs, [], [], [], feature1test, feature2test, testOutputs,
                   "train and test data")