import sys
from random import randint, random

from Ant import Ant
from Utils import length, computeNumerator, distance, probability


class ACO:

    def __init__(self, params, problParams):
        # initialize pheromone trails - 0
        self.__params = params
        self.__problParams = problParams
        self.__trails = [[1.0 for _ in range(0, problParams["noNodes"])] for _ in range(0, problParams["noNodes"])]
        # TODO ?number of ants
        self.__ants = []

    @property
    def problParams(self):
        return self.__problParams

    @property
    def params(self):
        return self.__params

    @property
    def trails(self):
        return self.__trails

    def initialisation(self):
        #self.__ants = [Ant(self.__problParams["noNodes"]) for _ in range(0, self.__params["noAnts"])]
        noAnts = round(self.__problParams["noNodes"] * self.__params["antFactor"])
        self.__ants = [Ant(self.__problParams["noNodes"]) for _ in range(0, noAnts)]
        for ant in self.__ants:
            ant.visit(randint(0, self.__problParams["noNodes"] - 1))

    # evaporation and lay pheromones on best trail
    def updateTrails(self):
        for p1 in range(0, self.__problParams["noNodes"]):
            for p2 in range(0, self.__problParams["noNodes"]):
                self.__trails[p1][p2] *= self.__params["evaporation"]

        ant = self.bestAntTrail()
        bestTrail = ant.trail
        pheromoneAmount = ant.pheromoneAmount / length(ant, self.__problParams["matrix"])
        for pos in range(0, len(bestTrail) - 1):
            self.__trails[bestTrail[pos]][bestTrail[pos + 1]] += pheromoneAmount

        self.__trails[len(bestTrail) - 1][0] += pheromoneAmount

    def updateTrailsOneStep(self, ant):
        self.__trails[ant.trail[ant.trailLength - 2]][ant.trail[ant.trailLength - 1]] += ant.pheromoneAmount

    # find best trail (distance-wise) and return ant
    def bestAntTrail(self):
        bestDistance = sys.maxsize
        bestAnt = None
        for ant in self.__ants:
            if length(ant, self.__problParams["matrix"]) < bestDistance:
                bestAnt = ant
                bestDistance = length(ant, self.__problParams["matrix"])
        return bestAnt

    def moveAnts(self):

        for _ in range(0, self.__problParams["noNodes"] - 1):
            for ant in self.__ants:
                city = self.nextCity(ant)
                ant.visit(city)
                self.updateTrailsOneStep(ant)

    def nextCity(self, ant):
        # decide if city is selected randomly or by fitness

        if random() < self.__params["randomFactor"]:
            # select random city
            while True:
                city = randint(0, self.__problParams["noNodes"] - 1)
                if not ant.isVisited(city):
                    return city

        probabs = self.probabilities(ant)
        r = random()
        total = 0
        for pos in range(0, self.__problParams["noNodes"]):
            total += probabs[pos]
            if total > r:
                return pos
        '''city = 0
        for pos in range(1, len(probabs)):
            if probabs[pos] > probabs[city]:
                city = pos
        return city'''

    # probability of being selected for each city
    def probabilities(self, ant):
        probabs = [0.0 for _ in range(0, self.__problParams["noNodes"])]

        #sum of pheromones on edges for possible destinations
        i = ant.trail[ant.trailLength - 1]
        pheromones = 0
        for pos in range(0, self.__problParams["noNodes"]):
            if not ant.isVisited(pos) and distance(i, pos, self.__problParams["matrix"]) != 0:
                pheromones += computeNumerator(self.__trails[i][pos],
                                               1.0 / distance(i, pos, self.__problParams["matrix"]),
                                               self.__params["pheromoneImportance"], self.__params["distancePriority"])

        for pos in range(0, self.__problParams["noNodes"]):
            if ant.isVisited(pos) and distance(i, pos, self.__problParams["matrix"]) != 0:
                probabs[pos] = 0.0
            elif distance(i, pos, self.__problParams["matrix"]) != 0:
                probabs[pos] = probability(self.__trails[i][pos],
                                           1.0 / distance(i, pos, self.__problParams["matrix"]),
                                           self.__params["pheromoneImportance"],
                                           self.__params["distancePriority"], pheromones)

        return probabs

    def applyPerturbation(self):

        p = randint(0, self.__problParams["noNodes"] // 4)
        for _ in range(0, p):
            n1 = randint(0, self.__problParams["noNodes"] - 1)
            n2 = randint(0, self.__problParams["noNodes"] - 1)
            self.__problParams["matrix"].itemset((n1, n2), 0)
            self.__trails[n1][n2] = 1.0

        for _ in range(0, p//2):
            n1 = randint(0, self.__problParams["noNodes"] - 1)
            n2 = randint(0, self.__problParams["noNodes"] - 1)
            self.__problParams["matrix"].itemset((n1, n2), 1000)
            self.__trails[n1][n2] = 1.0

