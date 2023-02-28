def ips_between(start, end):
    start_split = start.split(".")
    end_split = end.split(".")
    start = (int(start_split[0]) * 256 ** 3) + (int(start_split[1]) * 256 ** 2) + (int(start_split[2]) * 256) + (int(start_split[3]))
    end = (int(end_split[0]) * 256 ** 3) + (int(end_split[1]) * 256 ** 2) + (int(end_split[2]) * 256) + (int(end_split[3]))

    return end - start


test1 = ips_between("10.0.0.0", "10.0.0.50")  # 50
test2 = ips_between("20.0.0.10", "20.0.1.0")  # 246

print(test1)
print(test2)
