a = int(input("Enter number of rows: "))
n = 2*a-1
for i in range(1, a+1):
    for j in range(1, a-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
