def splitlist(list1):
    evenlist = []
    oddlist = []

    for i_loop in list1:
        if (i_loop % 2 == 0):
            evenlist.append(i_loop)
        else:
            oddlist.append(i_loop)

    print("Elements in the even list are : ")
    print(evenlist)
    print("Elements in the odd list are : ")
    print(oddlist)


list1 = []

size = int(input("Enter the number of elements in the Original List ::"))

print("Enter the elements of the Original List ::")
for i_loop in range(int(size)):
    ele = int(input(""))
    list1.append(ele)

splitlist(list1)
