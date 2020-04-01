import sys

from ACO import ACO
from Ant import Ant
from Utils import length


class UI:

    def __init__(self, aco):
        self.__ACO = aco

    def run(self):
        # self.__ACO.initialisation()
        bestTrailAnt = Ant(0)
        bestTrailDistance = sys.maxsize
        for step in range(0, self.__ACO.params["steps"]):
            if step % 20 == 0:
                self.__ACO.applyPerturbation()
            self.__ACO.initialisation()
            self.__ACO.moveAnts()
            # update pheromones for the best trail (Ant Colony System)
            self.__ACO.updateTrails()
            currentBestTrailAnt = self.__ACO.bestAntTrail()
            if length(currentBestTrailAnt, self.__ACO.problParams["matrix"]) < bestTrailDistance:
                bestTrailAnt = currentBestTrailAnt
                bestTrailDistance = length(currentBestTrailAnt, self.__ACO.problParams["matrix"])

            print("BEST TRAIL IN STEP " + str(step) + " : " + str(currentBestTrailAnt.trail) + " COST = " + str(
                length(currentBestTrailAnt,
                       self.__ACO.problParams["matrix"])))

        print("\nBEST TRAIL OVERALL: " + str(bestTrailAnt.trail) + " COST = " + str(
            length(bestTrailAnt, self.__ACO.problParams["matrix"])))
