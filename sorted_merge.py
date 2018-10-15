import random

def sorted_merge(arr_a, arr_b):
    i = len(arr_a) - len(arr_b) - 1
    j = len(arr_b) - 1
    k = len(arr_a) - 1
    while i >= 0 and j >= 0:
        if arr_a[i] >= arr_b[j]:
            arr_a[k] = arr_a[i]
            i -= 1
        else:
            arr_a[k] = arr_b[j]
            j -= 1
        k -= 1
    while i >= 0:
        arr_a[k] = arr_a[i]
        i -= 1
    while j >= 0:
        arr_a[k] = arr_b[j]
        j -= 1

def main():
    lo = 1
    hi = 100
    count = 10
    arr_c = [random.randint(lo, hi) for n in range(count)]
    arr_a = [None] * count
    arr_a[:count//2] = sorted(arr_c[:count//2])
    arr_b = sorted(arr_c[count//2:])
    sorted_merge(arr_a, arr_b)
    assert arr_a == sorted(arr_c), "array a is not sorted"

if __name__ == "__main__":
    main()

