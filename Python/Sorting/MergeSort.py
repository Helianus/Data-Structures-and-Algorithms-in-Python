# Merge Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Divide the input data into to two disjoint subsets
# recursively solve the problem
# merge the solutions

def merge_Sort(lst):
    n = len(lst)
    if n < 2:
        return                                                              # list is already sorted if it only contains single element
    
    # divide 
    mid = n // 2
    left = lst[0:mid]                                                       # copy of first half list
    right = lst[mid:n]                                                      # copy of second half list

    # conquer (recursively)
    merge_Sort(left)
    merge_Sort(right)

    # combain subsolutions (merge)
    merge(left, right, lst)

    return lst

# merge two sorted lists left and right into properly sized list
def merge(left, right, lst):
    i = j = 0                                                               # i and j represent the number of elements of each half list
    while i + j < len(lst):                                                 # sum of each length of half lists should not bigger than original one
        if j == len(right) or (i < len(left) and left[i] < right[j]):       # check if jth element of right half list reached the end
            lst[i + j] = left[i]                                            # copy ith element of left as next element of lst
            i += 1
        else:
            lst[i + j] = right[j]                                           # copy jth element of right as next item of lst
            j += 1