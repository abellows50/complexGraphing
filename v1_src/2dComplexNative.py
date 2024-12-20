#IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

#GETS EQUATION FROM FILE CALL
equation = sys.argv[1:][0]
print("f(input)=",equation)

#INITAILIZE VARIABLES TO HOLD COORDINATES
boardSize = 50
xlist = []
ylist=[]
zrlist = []
zclist = []

#TEST ALL COORDANATES
for x in range(-boardSize,boardSize):
  for y in range(-boardSize,boardSize):
    x = x*1
    y = y*1
    input = complex(x,y)
    try:
      z = eval(equation.replace('x','input'))
      xlist.append(x)
      ylist.append(y)
      zrlist.append(z.real)
      zclist.append(z.imag)
    except Exception as e: print(e)

xlist = np.array(xlist)
ylist = np.array(ylist)
zrlist = np.array(zrlist)

#CALCULATE OPACTITY SCALAR
scalar = max(max(zclist),abs(min(zclist)))
#SCALE
if scalar != 0:
  for i in range(len(zclist)):
    zclist[i] = zclist[i]/2/scalar + 0.5
else:
  for i in range(len(zclist)):
    zclist[i] = zclist[i] + 0.5

#PLOT DATA
zclist = np.array(zclist)
plt.scatter(xlist,ylist,c=zrlist, alpha=zclist)
plt.title("f(x)=" + equation)
plt.xlabel("Real")
plt.ylabel("Complex")
xlist,ylist,zrlist,zclist=[],[],[],[]

plt.show()