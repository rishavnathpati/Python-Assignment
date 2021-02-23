def factors(x):
    factor_list = []
    for i in range(1, x+1):
        if(x % i == 0):
            factor_list.append(i)
    return tuple(factor_list)


def main():
    number = int(input("Enter number to check if it is a perfect number: "))
    factor_tuple = factors(number)
    factor_sum = 0
    for each in range(len(factor_tuple)-1):
        factor_sum += factor_tuple[each]
    if(number == factor_sum):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")


if __name__ == "__main__":
    main()
