s = [2, 5, 6, 10, 1, 3, 12, 4]

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left_arr = [x for x in arr[1:] if x<=pivot]
    right_arr = [x for x in arr[1:] if x>pivot]
    return quick(left_arr)+[pivot]+quick(right_arr)


print(quick(s))
    