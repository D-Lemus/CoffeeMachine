import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

precios = np.array([1,2,3,4,8,9,104,5,6,7])

#Grafico de linea
#plt.plot(precios, marker="D")
#plt.title("Evolucion de precios")
#plt.show()

#Grafico de dispersion
x = np.arange(len(precios))
plt.scatter(x,precios, color="red")
plt.title("Precios vs Indice")
plt.show()
