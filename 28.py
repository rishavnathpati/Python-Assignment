def pascal(n):
    for line in range(1, n+1):
        co_eff = 1

        for i_loop in range(1, line+1):
            print(co_eff, end=" ")
            co_eff = int(co_eff*(line-i_loop)/i_loop)

        print("")


row_num = int(
    input("Enter the number of rows of Pascal's triangel you want to generate : "))
pascal(row_num)
