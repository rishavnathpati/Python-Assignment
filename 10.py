calls = int(input("Enter number of calls: "))
bill = 0

if calls <= 100:
    bill = calls*0.2

elif calls > 100 and calls <= 200:
    bill = 100*0.2+(calls-100)*0.3

else:
    bill = 100*0.2+100*0.3+(calls-200)*0.5

bill += 250

print("Total bill amount is", bill)
