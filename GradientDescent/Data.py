import csv

from utils import splitData


class Data:

    def __init__(self, filename, inputVariableNames, outputVariableName):
        self.__filename = filename
        self.__inputs, self.__outputs = self.readData(inputVariableNames, outputVariableName)
        self.__trainInputs, self.__trainOutputs, self.__testInputs, self.__testOutputs = splitData(self.__inputs, self.__outputs)

    def readData(self, inputVariableNames, outputVariableName):
        data = []
        dataNames = []
        inputs = []
        outputs = []
        with open(self.__filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    dataNames = row
                else:
                    data.append(row)
                line_count += 1
        for i in range(len(data)):
            currentData = []
            for name in inputVariableNames:
                index = dataNames.index(name)
                currentData.append(float(data[i][index]))
            inputs.append(currentData)
            outIndex = dataNames.index(outputVariableName)
            outputs.append(float(data[i][outIndex]))

        #return inputs, myMatrix(outputs)
        return inputs, outputs

    def myNormalisation(self):
        pass
    
    def sklearnNormalisation(self):
        pass

    @property
    def inputs(self):
        return self.__inputs

    @property
    def outputs(self):
        return self.__outputs

    @property
    def trainInputs(self):
        return self.__trainInputs

    @property
    def trainOutputs(self):
        return self.__trainOutputs

    @property
    def testInputs(self):
        return self.__testInputs

    @property
    def testOutputs(self):
        return self.__testOutputs
