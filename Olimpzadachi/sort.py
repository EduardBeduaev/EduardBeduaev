import time


def timer(func):
    def decorator(n):
        first = time.time()
        func(n)
        second = time.time()
        print(second - first)

    return decorator


@timer
def puzirek(a):
    c = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            c += 1
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    print("PUZIREK: c = ", c)


@timer
def podschetom(a):
    b = [0] * (max(a) + 1)
    c = 0
    for i in a:
        b[i] += 1
        c += 1
    res = []

    for i1 in range(len(b)):
        for i2 in range(b[i1]):
            res.append(i1)
            c += 1
    print("PODSCHETOM: c = ", c)


@timer
def tvoi(a):
    c = 0
    for i1 in range(len(a)):
        for i in range(len(a) - 1):
            c += 1
            if a[i] < a[i + 1]:
                pass
            else:
                a[i], a[i + 1] = a[i + 1], a[i]
    print("TVOI: c = ", c)


@timer
def quicksort(a, c):
    print("QUICKSORT: c = ", c)
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a) // 2]
        left = [x for x in a if x < pivot]
        right = [x for x in a if x > pivot]
        return quicksort(left, c + 1) + [pivot] + quicksort(right, c + 1)


a = [1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6,
     9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2,
     3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10,
     6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6,
     5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11,
     1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11, 1, 2, 3, 6, 5, 6, 9, 10, 6, 11]
puzirek(a)
podschetom(a)
tvoi(a)
quicksort(a, 0)
# puzirek - O(n ** 2)
# podschet - O(n * m)
# tvoi - O(n ** 2)
# quicksort - O(log n)
