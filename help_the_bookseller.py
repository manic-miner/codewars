list_of_art = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
list_of_cat = ["A", "B", "C", "D"]


def stock_list(list_of_art, list_of_cat):
    result = {}
    for item in list_of_art:
        key_letter = item[0]
        books_count = item[-3:]
        if item[0] in list_of_cat:
            result[key_letter] = int(books_count)
        print(result)
    # total_fstring = ""
    # for key_value in result:
    #     total_fstring.join(key_value)
    #     print(total_fstring)
    # return total_fstring


stock_list(list_of_art, list_of_cat)