import math
bees=int(input())
flowers=int(input())
honey=bees * flowers * 0.21
honeycombs=(honey//100.0)
h_honey=honey%100
print(f"{math.floor(honeycombs)} honeycombs filled.")
print(f"{h_honey:.2f} grams of honey left.")



