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


def solve(n):
    sum = 0
    for i in range(n):
        sum += primes[i]
    return sum


sieveSundaram(100000)
num = int(input("Enter a number to find nth prime sum: "))
print("Sum of prime numbers upto %f is %f" % (num, solve(num)))
