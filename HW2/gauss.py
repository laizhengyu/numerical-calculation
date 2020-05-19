import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


minx=0
maxx=4
miny=0
maxy=5

nx=40
ny=50

hx=(maxx-minx)/nx
hy=(maxy-miny)/ny

boundx1=50.0
boundx2=300.0
boundy1=75.0
boundy2=100.0

T=np.zeros((ny+1,nx+1))
e=np.zeros((ny+1,nx+1))
T[0,:]=boundx1
T[ny,:]=boundx2
T[:,0]=boundy1
T[:,nx]=boundy2

iteration=200
delta=10e-4

for i in range(iteration):
    for tx in range(1,nx):
        for ty in range(1,ny):
            temp=T[ty,tx]
            T[ty,tx]=(T[ty+1,tx]+T[ty-1,tx]+T[ty,tx+1]+T[ty,tx-1])/4
            e[ty,tx]=np.abs((temp-T[ty,tx])/T[ty,tx])
    if np.max(e)<delta:
        if i<iteration:
            print('convergent in :',i)
        break
       
# print(T)
# print(e)
X=np.arange(minx,maxx+hx,hx)
Y=np.arange(miny,maxy+hy,hy)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, T,cmap=plt.get_cmap('rainbow'))
plt.show()
