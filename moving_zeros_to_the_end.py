def move_zeros(lst):
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(number)
    return lst


test1 = (move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(test1)