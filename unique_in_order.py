def unique_in_order(sequence):
    uniques = []

    for element in sequence:
        if element in uniques[-1:]:
            pass
        else:
            uniques.append(element)
    return uniques


result = unique_in_order('AAAABBBCCDAABBBAABCCCC')
print(result)