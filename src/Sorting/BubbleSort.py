# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_Sort(lst):
    for i in range(len(lst)):
        print(lst)
        for j in range(1, len(lst) - i):
            if lst[j] < lst[j - 1]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst
