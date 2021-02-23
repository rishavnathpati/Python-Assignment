primes = []


def sieveSundaram(n):
    k = (n - 2) // 2
    integers_list = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers_list[i + j + 2 * i * j] = False
            j += 1
    if n > 2:
        primes.append(2)
    for i in range(1, k + 1):
        if integers_list[i]:
            primes.append(2*i + 1)
    findPrimes(n)


def findPrimes(n):
    if (n <= 2 or n % 2 != 0):
        print("Invalid Input")
        return

    i = 0
    while (primes[i] <= n // 2):
        diff = n - primes[i]
        if diff in primes:
            print(primes[i], "+", diff, "=", n)
            return
        i += 1


n = int(input("Enter a even number to check: "))
sieveSundaram(n)
