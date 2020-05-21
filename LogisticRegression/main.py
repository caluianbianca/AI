from cmath import exp

from Data import Data
from MyGradientDescent import MyGradientDescent
from MyLogisticRegression import MyLogisticRegression
from SklearnLogisticRegression import SklearnLogisticRegression
from UI import UI

data = Data("resources/iris.data")
logisticRegression = MyLogisticRegression()
#logisticRegression = SklearnLogisticRegression()
ui = UI(data, logisticRegression)
ui.run()




