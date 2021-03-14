whisky=float(input())
count_beer=float(input())
count_wine=float(input())
count_rakiq=float(input())
count_whisky=float(input())

price_rakiq=whisky/2
price_wine=price_rakiq -(price_rakiq * 0.40)
price_beer=price_rakiq -(price_rakiq * 0.80)
price_w=price_wine*count_wine
price_b=price_beer*count_beer
price_whisky=whisky*count_whisky
price_r=price_rakiq*count_rakiq
sum_all=price_r + price_b + price_w + price_whisky
print(f'{sum_all:.2f}')