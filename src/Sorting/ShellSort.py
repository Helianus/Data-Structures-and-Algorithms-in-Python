# Shell Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def shell_Sort(lst):
    gap = len(lst) // 2

    while gap > 0:
        
        # do insertion sort
        for i in range(gap, len(lst)):
            print(lst)
            cur = lst[i]
            j = i
            while j >= gap and cur < lst[j - gap]:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = cur
        gap //= 2
    return lst