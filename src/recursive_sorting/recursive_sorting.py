# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    first_index = 0
    second_index = 0
    for i in range(elements):
        if first_index >= len(arrA):
            merged_arr[i] = arrB[second_index]
            second_index +=1
        elif second_index >= len(arrB):
            merged_arr[i] = arrA[first_index]
            first_index += 1
        elif arrA[first_index] < arrB[second_index]:
            merged_arr[i] = arrA[first_index]
            first_index += 1
        else:
            merged_arr[i] = arrB[second_index]
            second_index +=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        # While your data set contains more than one item, split it in half
        mid_point = len(arr) //2
        left_side = arr[ : mid_point]
        right_side = arr[mid_point :]
        left = merge_sort(left_side)
        right = merge_sort(right_side)
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
