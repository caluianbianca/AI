import matplotlib.pyplot as plt
from numpy import reshape
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

from utils import myMatrix


class UI:

    def __init__(self, data, bgd):
        self.__data = data
        self.__bgd = bgd

    def run(self):

        # self.plotHistograms(self.__data.inputs, self.__data.outputs)
        # self.plotLiniarity(self.__data.inputs, self.__data.outputs)

        '''scaler = StandardScaler()
        scaler.fit(self.__data.trainInputs)
        trainInputs = scaler.transform(self.__data.trainInputs)
        testInputs = scaler.transform(self.__data.testInputs)
        trainOutputs = [[d] for d in self.__data.trainOutputs]
        testOutputs = [[d] for d in self.__data.testOutputs]
        scaler.fit(trainOutputs)  # fit only on training data
        normalisedTrainData = scaler.transform(trainOutputs)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testOutputs)  # apply same transformation to test data
        trainOutputs = [el[0] for el in normalisedTrainData]
        testOutputs = [el[0] for el in normalisedTestData]
        self.plotHistograms(trainInputs, trainOutputs)
        self.plotLiniarity(trainInputs, trainOutputs)
        self.__bgd.fit(trainInputs, trainOutputs)'''

        '''trainInputs = preprocessing.normalize(self.__data.trainInputs)
        trainOutputs = preprocessing.normalize(reshape(self.__data.trainOutputs,(-1, 1)))
        testInputs = preprocessing.normalize(self.__data.testInputs)
        testOutputs = preprocessing.normalize(reshape(self.__data.testOutputs, (-1, 1)))
        self.plotHistograms(trainInputs, trainOutputs)
        self.plotLiniarity(trainInputs, trainOutputs)
        self.__bgd.fit(trainInputs, trainOutputs)'''

        '''trainInputs = self.normalisation(self.__data.trainInputs)
        testInputs = self.normalisation(self.__data.testInputs)
        trainOutputs = self.normalisation(self.__data.trainOutputs)
        testOutputs = self.normalisation(self.__data.testOutputs)'''

        trainInputs, minFeatTrain1, maxFeatTrain1, minFeatTrain2, maxFeatTrain2 = self.normalisation(
            self.__data.trainInputs)
        trainOutputs, minFeatTest, maxFeatTest = self.normalisation(self.__data.trainOutputs)
        testInputs = self.normalisation(self.__data.testInputs, minFeatTrain1, maxFeatTrain1, minFeatTrain2,
                                        maxFeatTrain2)[0]
        testOutputs = self.normalisation(self.__data.testOutputs, minFeatTest, maxFeatTest)[0]

        # self.plotHistograms(self.__data.inputs, self.__data.outputs)
        # self.plotLiniarity(self.__data.inputs, self.__data.outputs)
        #self.plotTrainVsTest(trainInputs, testInputs, trainOutputs, testOutputs)
        self.__bgd.fit(trainInputs, trainOutputs)

        print("w0 = " + str(self.__bgd.intercept))
        print("w = " + str(self.__bgd.coefs))

        predictions = self.__bgd.predict(testInputs)
        predictionError = self.__bgd.predictionError(predictions, testOutputs)
        print("error = " + str(predictionError))

        self.plotModel(trainInputs, trainOutputs)

    def plotModel(self, inputs, outputs):
        gdpInputs = [values[0] for values in inputs]
        freedomInputs = [values[1] for values in inputs]

        w0, w1, w2 = self.__bgd.intercept, self.__bgd.coefs[0], self.__bgd.coefs[1]
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

    def plotLiniarity(self, inputs, outputs):
        gdpInputs = [values[0] for values in inputs]
        freedomInputs = [values[1] for values in inputs]
        outputs = [value for value in outputs]
        self.plot3Ddata(gdpInputs, freedomInputs, outputs, [], [], [], [], [], [], 'capita vs freedom vs happiness')

    def normalisation(self, inputs, minFeat1=None, maxFeat1=None, minFeat2=None, maxFeat2=None):
        if not isinstance(inputs[0], list):
            feature = inputs
            if minFeat1 is None and maxFeat1 is None:
                minFeat1 = min(feature)
                maxFeat1 = max(feature)
            scaledFeatures = [(feat - minFeat1) / (maxFeat1 - minFeat1) for feat in feature]

            return scaledFeatures, minFeat1, maxFeat1
        else:
            feature1 = [inputs[i][0] for i in range(len(inputs))]
            feature2 = [inputs[i][1] for i in range(len(inputs))]
            if minFeat1 is None and maxFeat1 is None:
                minFeat1 = min(feature1)
                maxFeat1 = max(feature1)
            scaledFeatures1 = [(feat - minFeat1) / (maxFeat1 - minFeat1) for feat in feature1]
            if minFeat2 is None and maxFeat2 is None:
                minFeat2 = min(feature2)
                maxFeat2 = max(feature2)
            scaledFeatures2 = [(feat - minFeat2) / (maxFeat2 - minFeat2) for feat in feature2]

            scaled = [[scaledFeatures1[i], scaledFeatures2[i]] for i in range(len(feature1))]
            return scaled, minFeat1, maxFeat1, minFeat2, maxFeat2

    def plotTrainVsTest(self, trainInputs, testInputs, trainOutputs, testOutputs):
        feature1train = [ex[0] for ex in trainInputs]
        feature2train = [ex[1] for ex in trainInputs]

        feature1test = [ex[0] for ex in testInputs]
        feature2test = [ex[1] for ex in testInputs]

        self.plot3Ddata(feature1train, feature2train, trainOutputs, [], [], [], feature1test, feature2test, testOutputs,
                        "train and test data (after normalisation)")
