def pattern(n):
    return '\n'.join((f'{number}' * number) for number in range(1, n+1))


test1 = pattern(5)  # "1\n22\n333\n4444\n55555"
print(test1)


