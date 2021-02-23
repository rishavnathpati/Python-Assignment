n = int(input("Enter a number to check for Automorphic: "))


def isAutomorphic(n):
    sq = n * n
    while (n > 0):
        if (n % 10 != sq % 10):
            return False

        n //= 10
        sq //= 10

    return True


if isAutomorphic(n):
    print("Automorphic")
else:
    print("Not Automorphic")
