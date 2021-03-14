figure=input()
area=0
import math
if figure=="square":
    side=float(input())
    area=side*side

elif figure=="rectangle":
    sideA=float(input())
    sideB=float(input())
    area=sideA * sideB

elif figure=="circle":
    r=float(input())
    area=math.pi * r * r

elif figure=="triangle":
    sideC=float(input())
    sideH=float(input())
    area=(sideC * sideH)/2


print(f"{area:.3f}")
