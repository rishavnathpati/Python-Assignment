n = int(input('Enter n : '))
prime = [True for i in range(n + 2)]
p = 2

while (p * p <= n + 1):
    if (prime[p] == True):
        for i in range(p * 2, n + 2, p):
            prime[i] = False
            p += 1

for p in range(2, n-1):
    if prime[p] and prime[p + 2]:
        print("(", p, ",", (p + 2), ")", end='')
