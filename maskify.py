def maskify(cc):
    mask = "#"
    return mask * len(cc[:-4]) + cc[-4:]


cc = input("Enter something to maskify: ")
print(f"Maskified: {maskify(cc)}")

