symbal_list = ["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"]


def grouping_method(data_list, left_data, right_data):
    length = len(symbal_list)
    left_list = data_list.count(left_data)
    right_list = data_list.count(right_data)

    start = 0
    end = length - 1

    while start < end:
        while start < end and data_list[start] == left_data:
            start += 1

        while start < end and data_list[end] == right_data:
            end -= 1

        data_list[start], data_list[end] = data_list[end], data_list[start]

    return data_list


data_list = grouping_method(symbal_list, "+", "-")
print(data_list)


def bubble_sort4(num_list):
    big_num = 0
    for i in range(int(len(num_list) / 2)):
        is_sorted = True
        for j in range(big_num, len(num_list) - big_num - 1, 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                is_sorted = False
        big_num += 1
        for k in range(len(num_list) - big_num - 1, big_num - 1, -1):
            if num_list[k] < num_list[k - 1]:
                num_list[k], num_list[k - 1] = num_list[k - 1], num_list[k]
                is_sorted = False

        if is_sorted:
            break
        print("num_list is %s" % num_list)
    return num_list


num_list = [8, 7, 6, 5, 4, 3, 2, 1]
num_list_inorder = bubble_sort4(num_list[:])
print("num_list_inorder is", num_list_inorder)
