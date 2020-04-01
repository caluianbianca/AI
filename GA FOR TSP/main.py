from random import seed

from GA import GA
from Repository import Repository
from TSPRepository import TSPRepository
from UI import UI


def main():
    #seed(1)
    #repository = Repository("E:\\ANUL II\\SEMESTRUL II\\INTELIGENTA ARTIFICIALA\\LABORATOR4\\resources\\easy_01_tsp.txt")
    repository = TSPRepository("resources/berlin52.txt")
    params = {'popSize': 100, 'noGen': 1000}
    ga = GA(params, repository.params)
    ui = UI(ga)
    ui.run()

main()