import math
record=float(input())
distance=float(input())
time_in_second=float(input())
swimming_time=distance * time_in_second
resistance=math.floor(distance / 15)
time_resistance=(resistance * 12.5)
all_time=swimming_time + time_resistance
if all_time<record:
    print(f" Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(abs(record-all_time)):.2f} seconds slower.")