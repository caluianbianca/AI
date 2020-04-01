from Utils import computeFitness


class Repository:

    __params = {}
    __filename = ""

    def __init__(self, filename):
        self.__filename = filename
        self.__params = self.__readData()

    @property
    def params(self):
        return self.__params

    def __readData(self):
        file = open(self.__filename, "r")
        matrix = []
        noNodes = int(file.readline())
        for line in file:
            costs = line.split(",")
            line = []
            for cost in costs:
                line.append(int(cost))
            matrix.append(line)
        params = {}
        params["noNodes"] = noNodes
        params["matrix"] = matrix
        params['function'] = computeFitness
        return params