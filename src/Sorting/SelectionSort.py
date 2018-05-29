# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Finding the minimal element continuously
# Move the minimal element to front
def selection_Sort(lst):
    for i in range(len(lst)):                                       # fist read
        print(lst)                                                  # print the sorting processes
        minIndex = i                                                # set the minimal index to be the first read
        for j in range(i + 1, len(lst)):                            # second read between the sorted elements and the end of the list
            if lst[j] < lst[minIndex]:                              # compare second read element and minimal index element
                minIndex = j                                        # set minimal index to be second read
                lst[minIndex], lst[i] = lst[i], lst[minIndex]       # swap
    return lst
