def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)


def calculateCombination(n, r):
    return factorial(n)//(factorial(r) * factorial(n-r))


def main():
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    print("nCr = \t ", calculateCombination(n, r))


if __name__ == "__main__":
    main()
