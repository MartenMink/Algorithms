def insertion_sort(array):
    """
    Сортировка вставками.
    Время работы алгоритма - O(n^2)
    """
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def merge_sort(array):
    """
        Сортировка слиянием.
        Время работы алгоритма - O(n*log(n))
    """
    def merge(a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        c = []
        while i < n or j < m:
            if (j == m) or (i < n and a[i] < b[j]):
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        return c
    def sort(a):
        n = len(a)
        if n < 2:
            return a
        al, ar = a[:n//2], a[n//2:]
        al, ar = sort(al), sort(ar)
        return merge(al, ar)


print(merge_sort([5, 4, 3, 3, 10, 8, 0, 56, -1, -2]))
