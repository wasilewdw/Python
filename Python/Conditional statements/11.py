num=float(input())
n_in=input()
n_out=input()
current_num=0
if n_in=="mm" and n_out=="m":
    current_num=num/1000
elif n_in=="mm" and n_out=="cm":
    current_num=num/10
elif n_in=="cm" and n_out=="m":
    current_num=num/100
elif n_in=="cm" and n_out=="mm":
    current_num=num*10
elif n_in=="m" and n_out=="cm":
    current_num=num*100
else:
    current_num=num*1000


print(f"{current_num:.3f}")


