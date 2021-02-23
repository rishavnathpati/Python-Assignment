def main():
    i1 = int(input("Enter a number: "))
    i2 = float(input("Enter a decimal number: "))
    i3 = input("Enter a string: ")
    original_tuple = (i1, i2, i3)
    print("Original tuple: \t ", original_tuple)
    intermediate_list = list(original_tuple)
    print("Intermediate list: \t ", intermediate_list)
    intermediate_list.append("App")
    new_tuple = tuple(intermediate_list)
    print("New tuple: \t\t ", new_tuple)


if __name__ == "__main__":
    main()
