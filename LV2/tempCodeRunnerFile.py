import numpy as np
a = np.array([6, 2, 9]) #napravi polje od tri elementa

print(type(a)) #prikaži tip polja
print(a.shape) #koliko elemenata ima vektor
print(a[0], a[1], a[2]) #prikaži prvi, drugi i treći element

a[1] = 5 #promijeni vrijednost polja na drugom mjestu
print(a) #prikaži cijeli a
print(a[1:2]) #izdvajanje
print(a[1:-1]) #izdvajanje

b = np.array([[3,7,1],[4,5,6]]) #napravi 2 dimenzionalno polje (matricu)

print(b.shape) #ispiši dimenzije polja
print(b) #ispiši cijelo polje b
print(b[0, 2], b[0, 1], b[1, 1]) #ispiši neke elemente polja
print(b[0:2,0:1]) #izdvajanje
print(b[:,0]) #izdvajanje

c = np.zeros((4,2))
d = np.ones((3,2)) 
e = np.full((1,2),5)
f = np.eye(2) 
g = np.array([1, 2, 3], np.float32)

duljina = len(g)
print(duljina)

h = g.tolist()
print(h)

c = g.transpose()
print(g)

np.concatenate((a, g,))

