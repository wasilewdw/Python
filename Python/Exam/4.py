import math
population=int(input())
years=int(input())

for i in range (1,years + 1):
    if i%5==0:
        current_population = math.floor(population // 10)
        current_population = current_population * 2
        population = population + current_population
        bees=math.floor(population//50)
        bees=bees * 5
        population=population - bees
        dead_bees = math.floor(population // 20)
        dead_bees = dead_bees * 2
        population = population - dead_bees
    else:
        current_population = math.floor(population // 10)
        current_population = current_population * 2
        population = population + current_population
        dead_bees = math.floor(population // 20)
        dead_bees = dead_bees * 2
        population = population - dead_bees


print(f"Beehive population: {population}")




