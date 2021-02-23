n = int(input("Enter a number: "))

sum = 0
while(n != 0):
    r = n % 10
    n = int(n/10)
    sum += r

print("Sum of digits: ", sum)
