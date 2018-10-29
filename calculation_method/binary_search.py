

def binary_search():
    pass


s = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]

# select_sort
for i in range(0, len(s) - 1):
    index = i
    for j in range(i + 1, len(s)):
        if s[index] > s[j]:
            index = j
            print(s)
    s[i], s[index] = s[index], s[i]

# print sort result.
print(s)