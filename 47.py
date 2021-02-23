def removeEmpty(full_list):
    new_list = []
    for each in full_list:
        if(len(each) == 0):
            continue
        new_list.append(each)
    return new_list


def main():
    original_list = [(), (1, "ss"), (), (), ('',), ("abcd", 1)]
    print("Original list: ", original_list)
    print("New list: ", removeEmpty(original_list))


if __name__ == "__main__":
    main()
