from collections import deque
from typing import List
def rotate_list(nums: List[int], n: int) -> List[int]:
    queue = deque(nums)
    for _ in range(n):
        queue.appendleft(queue.pop())
    return list(queue)
print(rotate_list([1, 2, 3, 4], 1))
