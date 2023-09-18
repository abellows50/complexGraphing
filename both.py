import numpy as np
from matplotlib import pyplot as plt
#import complex
#ZOOM:
import sys
import math

equation = sys.argv[1:][0]
print("f(input)=",equation)
boardSize = 25
interval = 1 #graph interval must be an int
plt.rcParams["figure.figsize"] = [6,4]
plt.rcParams["figure.autolayout"] = True
#fig, (ax1, my2d) = plt.subplots(1, 2)
fig = plt.figure()
my3d = fig.add_subplot(121, projection='3d')
my2d = fig.add_subplot(122)
#my2d = fig.add_subplot(111, projection='2d')

xlist = []
ylist=[]
zrlist = []
zclist = []
for x in range(-boardSize,boardSize,interval):
  for y in range(-boardSize,boardSize,interval):
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

xlist = np.array(xlist)
ylist = np.array(ylist)
zrlist = np.array(zrlist)

plt.title("f(x)=" + equation)

my3d.scatter(np.array(xlist),np.array(ylist),np.array(zrlist),c=np.array(zclist))

my3d.set_xlabel("Real")
my3d.set_ylabel("Complex")
my3d.set_zlabel("Real Part of Image")
scalar = max(max(zclist),abs(min(zclist)))

if scalar != 0:
  for i in range(len(zclist)):
    zclist[i] = zclist[i]/2/scalar + 0.5
else:
  for i in range(len(zclist)):
    zclist[i] = zclist[i] + 0.5

zclist = np.array(zclist)
my2d.scatter(xlist,ylist,c=zrlist, alpha=zclist)
my2d.set_xlabel("Real")
my2d.set_ylabel("Complex")

plt.show()