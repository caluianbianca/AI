import tsplib95
import networkx

from Utils import computeFitness


class TSPRepository:

    __params = {}
    __filename = ""

    def __init__(self, filename):
        self.__filename = filename
        self.__params = self.__readData()

    @property
    def params(self):
        return self.__params

    def __readData(self):
        data = tsplib95.load_problem(self.__filename)
        #networkx graph
        graph = data.get_graph()
        noNodes = graph.number_of_nodes()
        #numpy distance matrix
        matrix = networkx.to_numpy_matrix(graph)

        params = {}
        params["noNodes"] = noNodes
        params["matrix"] = matrix
        params["function"] = computeFitness

        return params

