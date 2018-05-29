# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Comparing adjacent elements by two for-loops continually
# Then move the bigger one to its back

def bubble_Sort(lst):
    for i in range(len(lst)):                                  # first read
        print(lst)                                             # print the sorting processes
        for j in range(1, len(lst) - i):                       # second read between the first element and the length of the list - first read
            if lst[j] < lst[j - 1]:                            # compare first read and second read
                lst[j], lst[j - 1] = lst[j - 1], lst[j]        # swap
    return lst
