class Ant:

    __visited = []
    __trail = []

    def __init__(self, tourSize):
        self.__visited = [False for _ in range(0, tourSize)]  # boolean
        self.__trail = []  # integer
        self.__trailLength = 0
        self.__pheromoneAmount = 500

    @property
    def trailLength(self):
        return self.__trailLength

    @property
    def trail(self):
        return self.__trail

    @property
    def visited(self):
        return self.__visited

    def isVisited(self, city):
        return self.__visited[city]

    @property
    def pheromoneAmount(self):
        return self.__pheromoneAmount

    def setPheromoneAmount(self, pheromoneAmount):
        self.__pheromoneAmount = pheromoneAmount

    def visit(self, city):
        self.__trail.append(city)
        self.__visited[city] = True
        self.__trailLength += 1
