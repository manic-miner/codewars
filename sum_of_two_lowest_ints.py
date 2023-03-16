
def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    return sum(sort[0:2])


test1 = sum_two_smallest_numbers([5, 8, 12, 18, 22])  # 13
print(test1)
