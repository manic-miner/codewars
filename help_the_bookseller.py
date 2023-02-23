# list_of_art = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# list_of_cat = ["A", "B"]

# list_of_art = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
# list_of_cat = ["A", "B", "C", "D"]

list_of_art = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
list_of_cat = ["A", "B", "C", "W"]


def stock_list(list_of_art, list_of_cat):
    result = {}
    for letter in list_of_cat:
        result[letter] = 0
        print(result)
    for item in list_of_art:
        key_letter = item[0]
        books_count = item[-3:]

        if key_letter in list_of_cat:
            result[key_letter] += int(books_count)
            print(result)

    if not list_of_art:
        return ""

    total_string = ""
    for key, value in result.items():
        string = f"({key} : {value})"
        total_string += f" - {string}"

        print(total_string[3:])
    return total_string[3:]


stock_list(list_of_art, list_of_cat)
