rows = int(input("Enter number of rows: "))

for num in range(rows+1):

    for i in range(num):

        print("*", end=" ")  # print number

    # line after each row to display pattern correctly

    print(" ")
