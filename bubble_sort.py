# O(N ^ 2)
# with added optimization if no swap is done then short circuit the loop

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        swap = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        if not swap:
            break
    return arr


arr = [10, 1, 2, 3, 4, 5]
bubble_sort(arr)
print(arr)
