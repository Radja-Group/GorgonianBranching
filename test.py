import random
import numpy as np
import matplotlib.pyplot as plt

N = 3 #number of steps
w = 2 #number of walkers

L = np.array([0])
x,y = [],[]
for iw in range(w):
	for iN in range(1,N):
		dx = np.random.randint(-1,2)
		dy = np.random.randint(-1,2)
		L[iw][iN][0] = L[iw][iN-1][0] + dx
		L[iw][iN][1] = L[iw][iN-1][1] + dy
print(L)
