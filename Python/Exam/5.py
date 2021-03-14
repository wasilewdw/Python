count_bees=int(input())
health=int(input())
attack=int(input())

while count_bees>=100:
    current_bees=count_bees - attack
    health=health -(current_bees * 5)
    if health<=0:
        print(f"Beehive won! Bees left {current_bees}.")
        break

    count_bees=current_bees
if count_bees<0:
    count_bees=0

if count_bees<100:
    print(f"The bear stole the honey! Bees left {abs(count_bees)}.")
