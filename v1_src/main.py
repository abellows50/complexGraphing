import os
#import complex
print("""
This is a complex graphing system that expands the domain of real function to ℤ. As such, the resulting graphs have 4 dimensions. The base of the graphs is a complex (a+bi) plane. In the 3d graph, the z axis is the real part of f(x) and the color represents the complex value with darker signifying a small value. In the 2d graph, the color signifies the real result and the opacity signifies the complex result of f(x).

To use, enter what f(x) should be equat to WITHOUT spaces. Make sure to utilize the python methods for math, ie instead of 2^6 write 2**6. At the present time, parenthesis are only supported in \ form ex: ( -> \( and all parenthesis must be sepperated by an operation.
""")

equation = input("f(x)=")



type = input("2d, 3d, or both: ")
if type == "3d":
  os.system(f"python 3dComplexNative.py {equation}")
elif type == "2d":
  os.system(f"python 2dComplexNative.py {equation}")
else:
  os.system(f"python both.py {equation}")
  

 