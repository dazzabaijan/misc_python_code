"""Binary search in a sorted list"""

def binary_search(array, value):
    """
    At each step, we reduce our search space by half.
    Compare middle value with search value.
    If search value < mid value, we search left side
    If search value > mid value, we search right side
    If we find search value, return index or return
    false otherwise.
    """
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

if __name__ == "__main__":
    print(binary_search([1,3,5,6,7], 5))