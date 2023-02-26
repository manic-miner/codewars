def spin_words(sentence):
    spinned_words = ""

    for word in sentence.split():
        print(word)
        if len(word) >= 5:
            word = word[::-1]
            spinned_words += word + " "
        else:
            spinned_words += word + " "
    return spinned_words.rstrip()


test1 = spin_words("sentence to split")
print(test1)