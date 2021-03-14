flowers=input()
count_flowers=int(input())
season=input()
quantity=0

if season=="Spring":
    if flowers=="Sunflower" or flowers=="Mint":
        quantity=count_flowers * 10
    elif flowers=="Daisy" or flowers=="Lavender":
        quantity=count_flowers * 12
elif season=="Summer":
    if flowers=="Sunflower" or flowers=="Daisy" or flowers=="Lavender":
        quantity=count_flowers * 8
    elif flowers=="Mint":
        quantity=count_flowers * 12
elif season=="Autumn":
    if flowers=="Daisy" or flowers=="Lavender" or flowers=="Mint":
        quantity=count_flowers* 6
    elif flowers=="Sunflower":
        quantity=count_flowers * 12

if season=="Summer":
    quantity=quantity * 1.10
if season=="Autumn":
    quantity=quantity * 0.95
if season=="Spring":
    if flowers=="Daisy" or flowers=="Mint":
        quantity=quantity * 1.10

print(f"Total honey harvested: {quantity:.2f}")