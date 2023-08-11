def recursive_selection_sort(arr, n):
    if n <= 1:
        return
    
    
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i
    

    arr[0], arr[min_index] = arr[min_index], arr[0]
    
    
    recursive_selection_sort(arr[1:], n - 1)


