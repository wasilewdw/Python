hours=int(input())
minutes=int(input())
import math
nhours=hours*60
time=nhours + minutes
time=time + 15
newHours=math.floor(time/60)
newMinutes=time%60
if newHours>=24:
    newHours=newHours -24

if newMinutes<10:
    print(f"{newHours}:0{newMinutes}")
else:
    print(f"{newHours}:{newMinutes}")
