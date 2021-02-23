def reverseTuple(inputTuple):
    return inputTuple[::-1]


def main():
    inputTuple = tuple(i.strip() for i in input(
        "Enter a tuple spaced with ',': ").split(','))
    print("Input Tuple: {}".format(inputTuple))
    print("Reversed Tuple: {}".format(reverseTuple(inputTuple)))


if __name__ == '__main__':
    main()