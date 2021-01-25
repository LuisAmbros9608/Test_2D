#Examen2_D Luis Hoil Ambros
"""
Programa Test_2D
Luis Alberto Hoil Ambros
Programa que traza dos rectagulos de la misma medida y un circulo
utilizando el ultimo digito de nuestro numero de control
número de control 18390050
"""

import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians #o usar la que ya trae numpy

plt. axis([0,30,30,0])
plt.axis('on')
plt.grid(True)

#_____Dibujar primer rectangulo
plt.plot([5,15],[5,5],linewidth=1,color='b')
plt.plot([5,15],[15,15],linewidth=1,color='b')
plt.plot([15,15],[15,5],linewidth=1,color='b')
plt.plot([5,5],[5,15],linewidth=1,color='b')

#_____Dibujar segundo rectangulo
plt.plot([10,20],[10,10],linewidth=1,color='b')
plt.plot([10,20],[20,20],linewidth=1,color='b')
plt.plot([10,10],[10,20],linewidth=1,color='b')
plt.plot([20,20],[10,20],linewidth=1,color='b')

#___Dibujar el circulo
xc=10
yc=10
r=5

p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=(.1,.5,.1))
    xlast=xp
    ylast=yp

plt.scatter(xc,yc,s=1,color=(.1,.5,.1))
plt.show()
