a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

hcf = 0
lcm = 0

if (a > b):
    x = a
else:
    x = b
for i in range(1, x):
    if (a % i == 0 and b % i == 0):
        hcf = i
print("HCF is: ", hcf)

lcm = (a*b)//hcf
print("lcm of both is: ", lcm)
