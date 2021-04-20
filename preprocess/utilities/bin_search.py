from .errors import DateNotFoundError


def bin_search(arr: list, item: str) -> int:
    l = 0
    r = len(arr) - 1

    while (l <= r):
        mid = (l + r) // 2
        val = arr[mid]
        val = val.split('.')[2]

        if (val == item):
            return mid
        elif (item < val):
            r = mid - 1
        elif (item > val):
            l = mid + 1

    raise DateNotFoundError()
