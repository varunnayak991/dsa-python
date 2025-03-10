def checkRotatedAndSorted(arr, n):
    """
    Checks if an array is sorted and rotated.

    Args:
      arr: The array to check.
      n: The length of the array.

    Returns:
      True if the array is sorted and rotated, False otherwise.
    """
    count = 0
    for i in range(2 * len(arr)):
        if arr[i % len(arr)] > arr[(i - 1) % len(arr)]:
            count += 1
            if count == len(arr) - 1:
                return True
        else:
            count = 0
    return False

print(checkRotatedAndSorted([6,71,2,3,4,5],5))
print(checkRotatedAndSorted([6,7,1,5,3,4,2],5))