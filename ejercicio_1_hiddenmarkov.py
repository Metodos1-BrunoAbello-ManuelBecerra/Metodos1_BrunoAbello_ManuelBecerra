import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

# Hidden Markov models, 1

States = np.array([0,1])
Prior =  np.array([0.2,0.8])

T = np.array([[0.8, 0.2], 
              [0.2, 0.8]])

E = np.array([[0.5, 0.9], 
              [0.5, 0.1]])

DictH = {0:'Justa',1:'Sesgada'}
DictO = {0:'Cara',1:'Sello'}
Obs = np.array([1,0,0,0,1,0,1,0])

#a

justa = 0.2 * 0.5**8
sesgada = 0.8 * 0.1 * 0.9**3 * 0.1 * 0.9 * 0.1 * 0.9

print("la probabilidad para esos eventos con una moneda justa es: "+str(justa*100)+ " por ciento")
print("la probabilidad para esos eventos con una moneda sesgada es: "+str(sesgada*100)+ " por ciento")

#b
def GetStates(States,N):
    
    CStates = list( combinations_with_replacement(States,N) )
    
    print(CStates)
    
    Permu = []
    
    for it in CStates:
        p = list(permutations(it,N))
       # print(p)
        
        for i in p:
            if i not in Permu:
                Permu.append(i)
                
    return np.array(Permu)

HiddenStates = GetStates(States,8)
print(HiddenStates)


def GetProb(T,E,Obs,State,Prior):
    
    n = len(Obs)
    p = 1.
    
    p *= Prior[State[0]]
    
    # Matriz de transicion
    for i in range(n-1):
        p *= T[ State[i+1], State[i]  ]
        
    for i in range(n):
        p *= E[ Obs[i], State[i] ]
        
    return p

P = np.zeros(HiddenStates.shape[0], dtype=np.float64)


for i in range(P.shape[0]):
    P[i] = GetProb(T,E,Obs,HiddenStates[i],Prior)
    
print(P)

plt.plot(P)

prob_max = np.max(P)
estado_max = HiddenStates[np.argmax(P)]

print("La mayor probabilidad es "+str(prob_max) +" lo cual corresponde a los eventos "+str(estado_max))

#c
ObsStates = GetStates([0,1],8)

Nobs = ObsStates.shape[0]

PObs = np.zeros(Nobs)

for j in range(Nobs):
    
    dim = HiddenStates.shape[0]
    P = np.zeros(dim)
    
    for i in range(dim):
        P[i] = GetProb(T,E,ObsStates[j],HiddenStates[i],Prior)
        
    PObs[j] = np.sum(P)
    

print(PObs)

#d
monedita = np.sum(PObs)
print("La suma de todos los estados observables es "+str(monedita))

#e

print("Sí depende ya que al cambiar las probabilidades a prior cambia la primera variable que multiplicas para la probablidad de una lista de eventos")

