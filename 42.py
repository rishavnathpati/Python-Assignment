def sumofdigits(x):
    sum = 0
    while(x > 0):
        sum += int(x % 10)
        x = int(x/10)
    return [int(d) for d in str(sum)]


n = int(input("Enter a number: "))

print(sumofdigits(n))
