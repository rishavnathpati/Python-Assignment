def fact(num):
    if num <= 0:
        return 1

    f = 1
    for i in range(1, num):
        f = f*i
    return f


x = int(input('Enter x : '))
n = int(input('Enter n : '))

series_sum = 0.0
i = 1
while i <= n:
    series_sum = series_sum + (x**i)/fact(i)
    i += 2

print("Series sum = ", series_sum)
