# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Assume first element is sorted at beginning
# and then using it to compare with next element
# if this element is less than next element
# then swap them
def insertion_Sort(lst):
    for i in range(1, len(lst)):            # first read from 1 to n
        print(lst)                          # print sorting processes
        cur = lst[i]                        # current element used to be inserted
        j = i                               # second read to find correct index j for current 
        while j > 0 and cur < lst[j - 1]:   # subsequence lst[j-1] 
             lst[j] = lst[j - 1]            # swap the element and its front
             j -= 1                         # read from back to head
        lst[j] = cur                        # current is in the right place
    return lst