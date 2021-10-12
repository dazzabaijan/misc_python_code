"""Rotating a list by K positions"""

def reverse_array(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1

def rotate_array(array, k):
    n = len(array)
    reverse_array(array, 0, k-1)
    reverse_array(array, k, n-1)
    reverse_array(array, 0, n-1)

def main():
    array = [i for i in range(1, 11)]
    rotate_array(array, 6)
    print(array)

if __name__ == "__main__":
    main()
