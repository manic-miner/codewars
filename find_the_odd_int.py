def find_it(seq):
    frequency = {}
    for i in seq:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    for k, v in frequency.items():
        if v % 2 == 0:
            pass
        else:
            return k

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
