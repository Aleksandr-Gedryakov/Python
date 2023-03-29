nums = [16, 380, 8, 1, 4, 211, 24, 117, 6, 8, 23]

"""
    nums.sort() - изменяет массив
    sorted(nums) не изменяет массив, но возвращает отсортированный
    
    Параметры:
    reverse - позволяет менять направление сортировки (Убывание/Возрастание)
    key - функция сортировки
    
"""


def len_num(x):
    return len(str(x))


# nums.sort(key=len_num) или при помощи lambda выражения
nums.sort(key=lambda x: len(str(x)))

print(nums)