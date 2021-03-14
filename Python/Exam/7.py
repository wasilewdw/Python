count_honey=int(input())
name=input()
current_sum=0
flag=False
while name!="Winter has come":

    sum=0
    for i in range(0,6):
        honey_count=float(input())
        sum+=honey_count
    if sum< 0:
            print(f"{name} was banished for gluttony")



    current_sum+=sum
    if current_sum>=count_honey:
        print(f"Well done! Honey surplus {current_sum - count_honey:.2f}.")
        flag=True
        break
    name=input()

if not flag:
    print(f"Hard Winter! Honey needed {count_honey - current_sum:.2f}.")




