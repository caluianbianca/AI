import sys

from Chromosome import Chromosome
from Utils import dist


class UI:
    def __init__(self, ga):
        self.__ga = ga

    @property
    def ga(self):
        return self.__ga

    def run(self):
        self.ga.initialisation()
        self.ga.evaluation()
        bestFitness = 0
        bestDist = 0
        bestChromoOverallRepres = None
        for g in range(self.ga.param['noGen']):
            self.ga.oneGenerationElitism()
            #self.ga.oneGeneration()
            #self.ga.oneGenerationSteadyState()
            bestChromo = self.ga.bestChromosome()
            if bestChromo.fitness > bestFitness:
                bestChromoOverallRepres = bestChromo.repres
                bestFitness = bestChromo.fitness
                bestDist = str(dist(bestChromo.repres, self.ga.problParam))
            print('Best solution in generation ' + str(g) + ' is: ' +
                  str(bestChromo.repres) + ' fitness = ' + str(bestChromo.fitness) + ' dist: ' + str(dist(bestChromo.repres, self.ga.problParam)))
        print("\n")
        print('Best solution overall is: ' +  str(bestChromoOverallRepres) + ' fitness = ' + str(bestFitness) + ' dist: ' + str(bestDist))