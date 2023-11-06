import sympy as sp

i = 1j

r0 = sp.Matrix([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, -1, 0],
              [0, 0, 0, -1]])


r1 = sp.Matrix([[0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, -1, 0, 0],
              [-1, 0, 0, 0]])


r2 = sp.Matrix([[0, 0, 0, -i],
              [0, 0, i, 0],
              [0, i, 0, 0],
              [-i, 0, 0, 0]])


r3 = sp.Matrix([[0, 0, 1, 0],
              [0, 0, 0, -1],
              [-1, 0, 0, 0],
              [0, 1, 0, 0]])

g = sp.Matrix([[1, 0, 0, 0],
              [0, -1, 0, 0],
              [0, 0, -1, 0],
              [0, 0, 0, -1]])


I4 = sp.Matrix([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

matrices = [r0,r1,r2,r3]

d = 0
for k in range(0,4):
    for j in range(0,4):

        m1 = matrices[k]
        m2 = matrices[j]
        
        a = m1 * m2 + m2 * m1
        b = 2 * g[k,j] * I4
        
        c = [k,j]
        
        if a.equals(b):
            d += 1
            print("este sirve "+ str(c))
            print(a)
            print(b)
        else: print("este no sirve "+ str(c))

print(d)

#note que en cada combinacion el algebra de Clifford esta dada por una relacion de anticonmutacion