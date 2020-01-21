# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for el in range(cur_index, len(arr)):
            if arr[el] < arr[smallest_index]:
                smallest_index = el
        #swap for the current smallest 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #check to see if list is sorted
    #did we have any swaps the last time through?
    #if no swaps then return the list
    have_swapped = True
    while have_swapped:
        #set swapped to false
        have_swapped = False
        #do the compare/swap thing
        #loop through the list
        for i in range (0, len(arr) -1):
            #is list[i] bigger than list[i + 1]?
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i+1], arr[i]
                #if a swap happens --set swapped true
                have_swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    max_num = maximum + 1
    count = [0] * max_num
    for el in arr:
        count[el] += 1
    i = 0
    for el in range(max_num):
        for c in range(count[el]):
            arr[i] = el
            i += 1
    return arr