list_of_art = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
list_of_cat = ["A", "B", "C", "D"]


def stock_list(list_of_art, list_of_cat):
    result = {}
    for item in list_of_art:
        key_letter = item[0]
        books_count = item[-3:]

        if key_letter in list_of_cat:
            result[key_letter] = int(books_count)
            print(result)
        elif key_letter == "":
            return ""
        else:
            result[key_letter] = 0
    total_string = ""
    for key, value in result.items():
        string = f"({key} : {value})"
        total_string += f" - {string}"

        print(total_string[3:])
    return total_string[3:]


stock_list(list_of_art, list_of_cat)