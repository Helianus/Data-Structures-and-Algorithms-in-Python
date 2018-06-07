# Quick Sort
# Time Complexity: O(n^2)
# Space Complexity: O(log(n))

# In-place quick sort does not create subsequences
# its subsequence of the input is represented by a leftmost and rightmost index
def quick_Sort(lst, first, last):
    print(lst)
    if first >= last:                               # the lst is sorted
        return
    pivot = lst[last]                               # last element of range is pivot
    lo = first                                      # scan from first to last
    hi = last - 1                                   # scan from last to first: "-1" is because of pivot
    while lo <= hi:
        while lo <= hi and lst[lo] < pivot:         # scan until reaching value >= pivot
            lo += 1
        while lo <= hi and pivot < lst[hi]:         # scan until reaching value <= pivot
            hi -= 1
        if lo <= hi:                                # check if scans did cross
            lst[lo], lst[hi] = lst[hi], lst[lo]     # swap
            # shrink range
            lo += 1
            hi -= 1                                 

    lst[lo], lst[last] = lst[last], lst[lo]         # re-setting pivot
    quick_Sort(lst, first, lo - 1)
    quick_Sort(lst, lo + 1, last)

    return lst
