def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = p0 * (1 + percent / 100) + aug
        p0 = int(p0)
        years += 1

    return years


test1 = nb_year(1500, 5, 100, 5000)  # 15
print(test1)