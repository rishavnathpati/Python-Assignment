def sortTupleList(tupleList):
    try:
        return sorted(tupleList, key=lambda tup: tup[1])
    except IndexError:
        print("A tuple may not have a second element")


def main():
    tupleList = list(tuple(j.strip() for j in input("Enter tuple number {} with a ',' separating each element: ".format(
        i+1)).split(',')) for i in range(int(input('Enter number of tuples: '))))
    print("Your tuple: {}".format(tupleList))
    print("Sorted by second element: {}".format(sortTupleList(tupleList)))


if __name__ == "__main__":
    main()
