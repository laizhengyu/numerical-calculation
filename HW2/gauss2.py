import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fun(x,y):
    return -x**3+3*x*y**2


minx=0
maxx=5
miny=0
maxy=5

nx=5
ny=5

hx=(maxx-minx)/nx
hy=(maxy-miny)/ny

#U=x^3-3xy^2

x=np.arange(0,maxx+hx,hx)
y=np.arange(0,maxy+hy,hy)
x,y=np.meshgrid(x,y)
U=fun(x,y)


boundx1=U[minx,:]
boundx2=U[maxx,:]
boundy1=U[:,minx]
boundy2=U[:,maxy]

T=np.zeros((nx+1,ny+1))
e=np.zeros((nx+1,ny+1))
T[0,:]=boundx1
T[nx,:]=boundx2
T[:,0]=boundy1
T[:,ny]=boundy2

iteration=200
delta=10e-4



for i in range(iteration):
    for tx in range(1,nx):
        for ty in range(1,ny):
            temp=T[tx,ty]
            T[tx,ty]=(T[tx+1,ty]+T[tx-1,ty]+T[tx,ty+1]+T[tx,ty-1])/4
            e[tx,ty]=np.abs((temp-T[tx,ty])/T[tx,ty])
    if np.max(e)<delta:
        if i<iteration:
            print('convergent in :',i)
        break


X=np.arange(minx,maxx+hx,hx)
Y=np.arange(miny,maxy+hy,hy)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, T,cmap=plt.get_cmap('rainbow'))
plt.show()

