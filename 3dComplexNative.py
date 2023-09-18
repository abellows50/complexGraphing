import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import math
#import complex
#ZOOM:
import sys

equation = sys.argv[1:][0]

print("f(input)=",equation)
boardSize = 25

plt.rcParams["figure.figsize"] = [6,4]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xlist = []
ylist=[]
zrlist = []
zclist = []
for x in range(-boardSize,boardSize):
  for y in range(-boardSize,boardSize):
    x = x*1
    y = y*1
    input = complex(x,y)
    
    try:
    ##COMPLEX SCATTERS##
    #z = sqrt(4-x^2)
      z = eval(equation.replace('x','input'))
      xlist.append(x)
      ylist.append(y)
      zrlist.append(z.real)
      zclist.append(z.imag)
    except Exception as e: print(e)
ax.scatter(np.array(xlist),np.array(ylist),np.array(zrlist),c=np.array(zclist))
ax.set_title("f(x)=" + equation)
ax.set_xlabel("Real")
ax.set_ylabel("Complex")
ax.set_zlabel("Real Part of Image")
    ##NON COMPLEX SCATTER##
    #z=x*y
    #ax.scatter(x,y,z,c='black')  
    #ax.scatter(x,y,0,c='black')
plt.show()