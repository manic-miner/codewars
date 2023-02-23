def dna_strand(dna):
    pairs = {"T": "A", "A": "T", "G": "C", "C": "G"}
    if dna not in pairs:
        print("Wrong value")
    else:
        return ''.join([pairs[x] for x in dna])


dna = input(">").upper()
print(f"{dna} --> {dna_strand(dna)}")