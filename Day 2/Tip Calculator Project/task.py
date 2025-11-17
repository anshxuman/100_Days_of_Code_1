print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
if (tip == 10):
    res = (bill / people) * 1.10
elif (tip == 12):
    res = (bill / people) * 1.12
elif (tip == 15):
    res = (bill / people) * 1.15

finall = round(res,2)
print(f"The tip to be paid : ${finall}")
