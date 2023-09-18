import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import math

plt.rcParams["figure.figsize"] = [6,4]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

class complex:
  def __init__(self, re, co):
    self.real = re
    self.complex = co
    if not re == 0:
      self.theta = math.atan(co/re)
    else:
      self.theta = 90
    self.r = math.sqrt(re**2+co**2)
  def congegate(self):
    return complex(self.real, -self.complex)
def positiveRoot(input):
  r = input.r
  theta = input.theta

  r = math.sqrt(r)
  theta = theta/2

  a = r*math.cos(theta)
  b = r*math.sin(theta)
  return complex(a,b)
def negitiveRoot(input):
  r = input.r
  theta = input.theta + 360

  r = math.sqrt(r)
  theta = theta/2

  a = r*math.cos(theta)
  b = r*math.sin(theta)
  return complex(a,b)
  
def add(complexA, complexB):
  complexOut = complex((complexA.real + complexB.real), (complexA.complex + complexB.complex))
  return complexOut

def subtract(complexA, complexB):
  complexOut = complex((complexA.real - complexB.real), (complexA.complex - complexB.complex))
  return complexOut
  
def multiply(complexA, complexB):
  realA = complexA.real
  complexValueA = complexA.complex
  complexValueB = complexB.complex
  realB = complexB.real
  outputReal = realA * realB - complexValueA * complexValueB
  outputComplex = complexValueA * realB + complexValueB * realA
  return complex(outputReal, outputComplex)
  
def divide(complexA, complexB):
  numerator = complexA
  denominator = complexB

  numerator = multiply(numerator, denominator.congegate())
  denominator = multiply(denominator, denominator.congegate())

  realOut = numerator.real/denominator.real
  complexOut = numerator.complex/denominator.real
  return complex(realOut, complexOut)

boardSize = 10
for x in range(-boardSize,boardSize):
  for y in range(-boardSize,boardSize):
    x = x*1
    y = y*1
    input = complex(x,y)
    
    
    ##COMPLEX SCATTERS##
    #z = sqrt(4-x^2)
    z = positiveRoot(subtract(complex(4,0),multiply(input, input)))
    z2 = negitiveRoot(subtract(complex(4,0),multiply(input, input)))
    ax.scatter(x,y,z.real, c='red')
    ax.scatter(x,y,z2.real,c='blue')

    ##NON COMPLEX SCATTER##
    #z=x*y
    #ax.scatter(x,y,z,c='black')  
    #ax.scatter(x,y,0,c='black')
plt.show()