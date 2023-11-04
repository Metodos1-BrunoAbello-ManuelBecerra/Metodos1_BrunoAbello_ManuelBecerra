import numpy as np

#PROBLEMA 6

R = 0.5 #cm
a = 0.01 #cm
#error < 0.5%
Real = np.pi * (R - np.sqrt(R**2 - a**2))
print("El valor real es " +str(Real))
f = lambda x: ((np.sqrt(a**2 - x**2))/(R+x))

class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.
        
class Simpson(Integrator):
    
    def __init__(self,x,f):
        Integrator.__init__(self,x,f)
        
    def GetIntegral(self):
        
        self.Integral = 0.
        
        self.Integral += self.y[0] + self.y[-1]
        
        for i in range( len(self.y[1:-1]) ):
            
            if i%2 == 0:
                self.Integral += 4*self.y[i+1]
            else:
                self.Integral += 2*self.y[i+1]
          
        return self.Integral*self.h/3
    
    def GetDerivative(self):
        
        d = f(self.x + 2*self.h) - 4*f(self.x + self.h) + 6*f(self.x) - 4*f(self.x - self.h) + f(self.x - 2*self.h)
        d /= self.h**4
        
        
        return d
    
    def GetError(self):
        
        d = self.GetDerivative()
        max_ = np.max(np.abs(d))
        
        self.error = (self.x[-1]-self.x[0])*self.h**4*max_/180
        
        return self.error

N = 1000
x = np.linspace(-a,a,N+1)

Integrador = Simpson(x,f)
aprox = Integrador.GetIntegral()
print("La aproximacion " + str(aprox))

error = np.abs((aprox - Real)/Real)*100

print("El error es "+str(error)+ "% y como pueden ver es mucho menos que 5%")