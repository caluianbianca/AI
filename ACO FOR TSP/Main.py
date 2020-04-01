from random import seed

from ACO import ACO
from Repository import Repository
from UI import UI

def run():

        params = {"evaporation": 0.1, "distancePriority": 2, "pheromoneImportance": 0.1, "randomFactor": 0.3, "steps": 100, "antFactor": 0.9}
        repository = Repository("resources/eil51.txt")
        aco = ACO(params, repository.params)
        ui = UI(aco)

        ui.run()
seed(1)
run()