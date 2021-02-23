n = int(input("Enter nth number: "))
num = 0
f = [0, 1]
for i in range(2, n+1):
    num = (f[i-1] + f[i-2])
    if(num <= n):
        f.append(num)
    else:
        break

print("a) Fibonacci series upto n: ", f)

f = [0, 1]
for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])

print("b) nth Fibonacci number: ", f[n-1])
print("c) First n Fibonacci number: ", f)