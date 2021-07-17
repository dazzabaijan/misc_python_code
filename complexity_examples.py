"""Time complexity examples"""

def fun1(n):
    """
    Time Complexity: O(n)
    """
    m = 0
    i = 0
    while i < n:
        m += 1
        i += 1
    return m


def fun2(n):
    """
    Time Complexity: O(n^2)
    """
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m


def fun3(n):
    """
    Time Complexity: O(n+(n-1)+(n-2)+...) = O(n(n+1)/2) = O(n^2)
    """
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < i:
            m += 1
            j += 1
        i += 1
    return m


def fun4(n):
    """
    Time Complexity: O(log(n))
    Each time problem space is divided into half.
    """
    m = 0
    i = 1
    while i < n:
        m += 1
        i = i*2
    return m


def fun5(n):
    """
    Time Complexity: O(log(n))
    Each time problem space is divided in half.
    """
    m = 0
    i = n
    while i > 0:
        m += 1
        i = i/2
    return m


def fun6(n):
    """
    Time Complexity: O(n^3)
    Three nested loops with each loop running n iterations.
    """
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            k = 0
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m


def fun7(n):
    """
    Time Complexity: T(n) = O(n^2) + O(n^2) = O(n^2)
    Two groups of loop are consecutive, hence their complexities
    will add up to a final complexity.
    """
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    i = 0
    while i < n:
        k = 0 
        while k < n:
            m += 1
            k += 1
        i += 1
    return m


def fun8(n):
    """
    Time Complexity: O(n*sqrt(n)) = O(n^(3/2))
    """
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < math.sqrt(n):
            m += 1
            j += 1
        i += 1
    return m


def fun9(n):
    """
    Time Complexity: O(log(n))
    Each time problem space is divided into half.
    """
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m += 1
            j += 1
        i /= 2
    return m


def fun10(n):
    """
    Time Complexity: O(n+(n-1)+(n-2)+...) = O(n(n+1)/2) = O(n^2)
    Arithmetic Progression
    """
    m = 0
    i = 0
    while i < n:
        j = i
        while j > 0:
            m += 1
            j -= 1
        i += 1
    return m


def fun11(n):
    """
    Time Complexity: O(n^3)
    """
    m = 0
    i = 0
    while i < n:
        j = i
        while j < n:
            k = j + 1
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m


def fun12(n):
    """
    Time Complexity: O(n)
    j value is not reset at each iteration
    """
    m = 0
    n = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1
    return m


def fun13(n):
    """
    Time Complexity: T(n) = O(1 + 2 + 4 +...+ n/2 + n) = O(n)
    The inner loop will run for 1, 2, 4, ..., n times in successive
    iteration of the outer loop.
    """
    m = 0
    i = 1
    while i <= n:
        j = 0
        while k <= i:
            m += 1
            j += 1
        i *= 2
    return m