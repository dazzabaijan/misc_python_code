"""Binary search in a sorted list"""

def binary_search(array, value):
    size = len(array)
    low = 0
    high = size - 1
    while low <= high:
        mid = int(low + (high - low)/2)
        if array[mid] == value:
            return True
        else:
            if array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    return False

print(binary_search([1,3,5,6,7], 5))