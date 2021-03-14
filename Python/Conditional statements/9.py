import math
budget=float(input())
count_extras=float(input())
price_clothing=float(input())
price_decor=0.1 * budget
price_for_wear=count_extras * price_clothing
if count_extras>150:
    price_for_wear=price_for_wear * 0.90

sum=price_decor + price_for_wear
if sum>budget:
    print("Not enough money!")
    print(f"Wingard needs {(abs(budget-sum)):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(abs(budget-sum)):.2f} leva left.")
