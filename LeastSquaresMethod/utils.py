import numpy


def splitData(inputs, outputs):
    numpy.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = numpy.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    return trainInputs, trainOutputs, testInputs, testOutputs


def myMatrix(data):
    matrix = []
    for el in data:
        matrix.append([el])

    return matrix
