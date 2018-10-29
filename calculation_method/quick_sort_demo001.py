def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])


print (sum([]))
print (sum([2, ]))
print (sum([2, 4, 6]))

print('-' * 20)


def count_list(list):
    if list == []:
        return 0
    else:
        return 1 + count_list(list[1:])


print (count_list([]))
print (count_list([2]))
print (count_list([2, 4]))
print (count_list([2, 4, 6]))

print('-' * 20)


def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] if list[0] > find_max(list[1:]) else find_max(list[1:])


# print (find_max([]))
print (find_max([2]))
print (find_max([2, 4]))
print (find_max([2, 4, 6]))
