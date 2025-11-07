def binary_search(arr : list[int], target: int) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < arr[mid]:
            hi = mid - 1
        elif target > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return lo #Correct position if not found