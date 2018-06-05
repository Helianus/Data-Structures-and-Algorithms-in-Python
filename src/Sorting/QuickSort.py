# Quick Sort
# Time Complexity: O(n^2)
# Space Complexity: O(log(n))

def quick_Sort(lst, first, last):
    print(lst)
    if first >= last:
        return
    pivot = lst[last]
    lo = first
    hi = last - 1
    while lo <= hi:
        while lo <= hi and lst[lo] < pivot:
            lo += 1
        while lo <= hi and pivot < lst[hi]:
            hi -= 1
        if lo <= hi:
            lst[lo], lst[hi] = lst[hi], lst[lo]
            lo, hi = lo + 1, hi - 1

    lst[lo], lst[last] = lst[last], lst[lo]
    quick_Sort(lst, first, lo - 1)
    quick_Sort(lst, lo + 1, last)

    return lst

lst = [4, 0, 3, 2, 1, 5, 8, 9, 7, 6]
print(quick_Sort(lst, 0, len(lst) - 1))