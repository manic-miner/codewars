def likes(names):
    length = len(names)
    variants = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    return variants[min(4, length)].format(*names[:3], others=length-2)


test1 = likes([])  # 'no one likes this'
test2 = likes(['Peter'])  # 'Peter likes this'
test3 = likes(['Jacob', 'Alex'])  # 'Jacob and Alex like this'
test4 = likes(['Max', 'John', 'Mark'])  # 'Max, John and Mark like this'
test5 = likes(['Alex', 'Jacob', 'Mark', 'Max'])  # 'Alex, Jacob and 2 others like this'
print(test1, test2, test3, test4, test5, sep="\n")

