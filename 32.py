def factorial(num):
    if (num == 0):
        return 1
    elif (num == 1):
        return 1
    else:
        return num*factorial(num-1)


n = int(input("Enter the number whose factorial you want to find : "))

print("The factorial of the number is {}".format(factorial(n)))
