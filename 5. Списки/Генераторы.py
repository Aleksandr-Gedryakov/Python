# Для формирования списков можно использовать генераторы
from random import randint

nums1 = [i for i in range(50) if i % 3 == 0]
nums2 = [i ** 2 for i in range(10)]
nums3 = [randint(1, 50) for _ in range(10)]

print(nums3)