rows = int(input("Enter number of rows: "))

for row in range(1, rows+1):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1
    print("")
