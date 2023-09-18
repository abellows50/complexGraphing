import math
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
def raiseTo(z,exponent):
  output = complex(1,0)
  for i in range(exponent):
    output = multiply(z, output)
  return output
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
