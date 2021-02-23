def sumUptoN(n):
    if(n == 1):
        return 1
    return n + sumUptoN(n-1)


def main():
    limit = int(
        input("Enter n, limit till which sum of natural numbers is to be found: "))
    print("Sum of natural numbers upto " + str(limit) + ": ", sumUptoN(limit))


if __name__ == "__main__":
    main()
