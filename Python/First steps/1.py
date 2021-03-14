days=int(input())
count_cook=int(input())
torta=int(input())
gof=int(input())
palach=int(input())
sum_one_torta=torta*45
sum_one_gof=gof*5.80
sum_one_palach=palach*3.20
sum_all_cook=(sum_one_gof + sum_one_palach + sum_one_torta)*count_cook
sum=sum_all_cook*days
sum_without=sum - (sum/8)
print(f'{sum_without:.2f}')
