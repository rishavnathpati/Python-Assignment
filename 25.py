def prime(num):
    flag = True
    for i in range(2, num): 
        if num % i == 0:
            flag = False
            break
    return flag

def fibonacci(num):
    return num if num<= 1 else (fibonacci(num-1)+fibonacci(num-2))

def findPrimeFibonacchi(num):
    sequence = [fibonacci(i) for i in range(num)]
    primeList = [i for i in sequence if prime(i) and i>1]
    return sequence, primeList

def main():
    fibSeq, primeSeq = findPrimeFibonacchi(int(input("Enter number of Fibonacchi terms: ")))
    print("Fibonacchi Sequence:  {}\nPrime Fibonacchi Sequence:  {}".format(fibSeq, primeSeq))

if __name__ == "__main__":
    main()