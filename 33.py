def fibonacci(num):
    return num if num <= 1 else (fibonacci(num-1)+fibonacci(num-2))


def nthFib(num):
    sequence = [fibonacci(i) for i in range(num)]
    return sequence[len(sequence)-1]


def main():
    print("Nth Fibonacchi number: {}".format(
        nthFib(int(input("Enter a number: ")))))


if __name__ == "__main__":
    main()
