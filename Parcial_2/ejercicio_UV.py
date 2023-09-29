import numpy as np
c=3*((10)**8)
h = 6.626*((10)**-34)
k = 1.3806*((10)**-23)
T = 5772
n = 20
#Punto a
lamda0 =  1*((10)**-7)
lamda1 = 4*((10)**-7) #m

v0 = c/lamda0
v1 = c/lamda1

a = (h*v0)/(k*T)
b = (h*v1)/(k*T)
f = lambda x: (x**3)/(-np.exp(-x)+1)

Roots, Weights = np.polynomial.legendre.leggauss(n)

t = 0.5*( (b-a)*Roots + a + b ) #ese b-a es donde se define el intervalo
Inum = 0.5*(b-a)*np.sum(Weights*f(t))
print(Inum)

#Punto b

Zeros, Weights = np.polynomial.laguerre.laggauss(n)
#Definimos los ceros y los pesos de Legendre, una cuadratura adecuada para el denominador
f = lambda x: (x**3)/(-np.exp(-x)+1)
#Definimos la función, que ha sido ajustada para poder realizar la suma según la cuadratura
#de Gauss-Laguerre
Iden = np.sum(f(Zeros)*Weights)
#Realizamos la suma y encontramos la integral
print (Iden)


#Punto C
f = Inum/Iden
print (f)


#Punto E

#La diferencia de porcentaje entre lo explicado por el IDEAM y lo encontrado en el cálculo
#se debe al hecho que, cuando hacemos el cálculo, estamos buscando la porción de rayos UV
#que están llegando a la tierra. 
#Sin embargo, los detectores del IDEAM no se encuentran fuera de la atmósfera, sino debajo.
#El trabajo de la atmósfera es frenar parte de los rayos Ultra Violeta que llegan al planeta.
#Es decir, si bien el planeta recibe un 12% de rayos Ultra Violeta, la atmósfera frena un
#4.8% de estos a la altura de Bogotá. Si nos acercamos más al nivel del mar, este porcentaje
#bloqueado será mayor.