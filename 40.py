import collections


def count(tuple_list):
    flag = False
    value = collections.Counter(tuple_list)
    uniq_list = list(set(tuple_list))

    for i_loop in uniq_list:
        if (value[i_loop] >= 2):
            flag = True
            print(i_loop, " is repeated ", value[i_loop], " times")

    if (flag == False):
        print("Repeated items do not exist")


tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('a', 'b'), ('e', 'f')]
count(tuple_list)
