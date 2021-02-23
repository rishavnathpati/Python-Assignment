n = int(input("Enter a number: "))

rev = 0
while(n != 0):
    r = n % 10
    n = int(n/10)
    rev = rev*10 + r

print("Sum of digits: ", rev)
