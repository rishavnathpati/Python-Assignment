n = int(input("Enter a number: "))
c = 0
for i in range(1, n+1):
    if(n % i == 0):
        c += 1

if(c > 2):
    print("Composite number")
else:
    print("Prime number")
