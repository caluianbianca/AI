from Data import Data
from MyBGD import MyBGD
from SklearnBGD import SklearnBGD
from UI import UI

data = Data("resources/world-happiness-report-2017.csv", ["Economy..GDP.per.Capita.", "Freedom"], "Happiness.Score")
bgd = MyBGD()
#bgd = SklearnBGD()
ui = UI(data, bgd)
ui.run()