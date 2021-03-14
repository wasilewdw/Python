intellect=int(input())
force=int(input())
sex=input()
role=""

if intellect>=80 and force>=80 and sex=="female":
    role="Queen Bee"
elif intellect>=80:
    role="Repairing Bee"
elif intellect>=60:
    role="Cleaning Bee"
elif force>=80 and sex=='male':
    role="Drone Bee"
elif force>=60:
    role="Guard Bee"
else:
    role="Worker Bee"


print(role)