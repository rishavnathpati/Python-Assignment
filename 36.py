def gcd(first, second):
    if (first == 0):
        return second
    if (second == 0):
        return first
    if (first == second):
        return first
    if (first > second):
        return gcd(first-second, second)
    return gcd(first, second-first)


first = int(input("Enter the first number : "))
second = int(input("Enter the second number : "))

print("The Greatest Common Divisor of the two numbers is {}".format(gcd(first, second)))
