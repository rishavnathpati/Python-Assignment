def Factors(num):
    factorList = [i for i in range(1, num+1) if num % i == 0]
    return factorList


def prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


def primeFact(num):
    return [i for i in Factors(num) if prime(i) and i > 1]


def main():
    print("Prime Factors are: {}".format(
        primeFact(int(input("Enter a number: ")))))


if __name__ == "__main__":
    main()
