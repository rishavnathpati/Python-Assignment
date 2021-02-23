def power(a, b):
    if(b == 1):
        return a
    return a * power(a, b-1)


def main():
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    print(str(base) + "^" + str(exponent) + " = ", power(base, exponent))


if __name__ == "__main__":
    main()
