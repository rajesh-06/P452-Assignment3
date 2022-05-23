import mm1
import matplotlib.pyplot as plt
import numpy as np 
import math
import copy

def laplace(A, steps, eps=1e-4):
 
    ny = len(A)
    k = 0
    diff = eps + 1
    
    while k < steps and diff > eps:
        A1 = copy.deepcopy(A)
        diff = 0.0
        for y in range(1,ny-1):
            for x in range(1,ny-1):
                A[y][x] = (A1[y][x+1] + A1[y][x-1] + A1[y+1][x] + A1[y-1][x])/4
                diff  = diff + abs(A[y][x] - A1[y][x])

        diff = diff /(ny**2)
        k = k + 1
        #print(k)
    return(A)
n=100
L=mm1.zeromatrix(n,n)
for i in range(len(L[-1])):
	L[0][i]=1
#print(L)
L1=copy.deepcopy(L)

eps = 0.00001
steps = 500
L2= laplace(L,steps,eps)


fig, axs = plt.subplots(1,2)

ax=axs[0]
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Initial condition')
pcm=ax.pcolormesh(L1,cmap='RdBu_r')
ax=axs[1]
pcm=ax.pcolormesh(L2,cmap='RdBu_r')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Final')
fig.colorbar(pcm,ax=ax)
plt.show()
