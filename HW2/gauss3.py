#以此为准
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fun(x,y):
    return -x**3+3*x*y**2

minx=0
maxx=10
miny=0
maxy=10
E=[]
a=5
for j in range(1,a+1):
    nx=5*j
    ny=5*j
    
    hx=(maxx-minx)/nx
    hy=(maxy-miny)/ny
    
    iteration=20000
    delta=10e-4
        
    x=np.arange(0,maxx+delta,hx)
    y=np.arange(0,maxy+delta,hy)
    x,y=np.meshgrid(x,y)
    U=fun(x,y)
    
    
    boundx1=U[0,:]
    boundx2=U[nx,:]
    boundy1=U[:,0]
    boundy2=U[:,ny]
    
    T=np.zeros((nx+1,ny+1))
    e=np.zeros((nx+1,ny+1))
    T[0,:]=boundx1
    T[nx,:]=boundx2
    T[:,0]=boundy1
    T[:,ny]=boundy2
    
    
    Oh=[]
    
    for i in range(iteration):
        for tx in range(1,nx):
            for ty in range(1,ny):
                temp=T[tx,ty]
                T[tx,ty]=(T[tx+1,ty]+T[tx-1,ty]+T[tx,ty+1]+T[tx,ty-1])/4
                e[tx,ty]=np.abs((temp-T[tx,ty])/T[tx,ty])
                
        Oh.append(U[nx//2 ,ny//2  ]-T[nx//2,ny//2])     
        if np.max(e)<delta:
            E.append(U-T)
            if i<iteration:
                ite=i
                convergence=np.array(Oh)
                
                plt.plot(np.arange(0,ite+1),convergence)
                print(nx//5,'times ','convergent in :',i)
            break


E2=U-T

X=np.arange(minx,maxx+hx,hx)
Y=np.arange(miny,maxy+hy,hy)
X, Y = np.meshgrid(X, Y)

#%%    
fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(x, y, T,cmap=plt.get_cmap('rainbow'))
ax = fig.add_subplot(132, projection='3d')
ax.plot_surface(x, y, U,cmap=plt.get_cmap('rainbow'))
ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(x, y,E2 ,cmap=plt.get_cmap('rainbow'))
plt.show()




