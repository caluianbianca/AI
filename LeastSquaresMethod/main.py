from Data import Data
from MyLinearMultivariateRegression import MyLinearMultivariateRegression
from SklearnLinearMultivariateRegression import SklearnLinearMultivariateRegression
from UI import UI

data = Data("resources/world-happiness-report-2017.csv", ["Economy..GDP.per.Capita.", "Freedom"], "Happiness.Score")
#regression = MyLinearMultivariateRegression()
regression = SklearnLinearMultivariateRegression()
ui = UI(data, regression)
ui.run()
