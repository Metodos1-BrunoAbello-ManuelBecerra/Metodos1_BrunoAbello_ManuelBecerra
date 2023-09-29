import numpy as np

n = 20



#Punto b
Zeros, Weights = np.polynomial.legendre.leggauss(n)
#Definimos los ceros y los pesos de Legendre, una cuadratura adecuada para el denominador
f = lambda x: (x**3)/(np.exp(-x)-1)
#Definimos la función, que ha sido ajustada para poder realizar la suma según la cuadratura
#de Gauss-Laguerre
Iden = np.sum(f(Zeros)*Weights)
#Realizamos la suma y encontramos la integral
print (Iden)