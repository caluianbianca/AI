from Data import Data
from KMeans import KMeans
from UI import UI

data = Data("resources/iris.data")
classifier = KMeans(3)
ui = UI(classifier, data)
ui.run()