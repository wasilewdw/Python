import math
income=float(input())
grade=float(input())
salary=float(input())

scholarship=0
social_sscholarship=0
if income<salary:
    if grade>4.50:
        social_sscholarship=0.35 * salary

if grade>=5.50:
    scholarship=grade*25

if social_sscholarship > scholarship:
    print(f"You get a Social scholarship {math.floor(social_sscholarship)} BGN")
elif social_sscholarship < scholarship:
    print(f"You get a scholarship for excellent results {math.floor(scholarship)} BGN")
else:
    print("You cannot get a scholarship!")



