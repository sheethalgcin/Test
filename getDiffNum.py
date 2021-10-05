from typing import List, Any


def get_different_number(arr):
    n = len(arr)
    airport= sorted(arr)

    for i in range(n - 1):
        if i != airport[i]:
            return i
    return n


arr =[0,2,3,4]
m= get_different_number(arr)
print(m)
