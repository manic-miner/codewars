def pig_it(text):
    pig_latin = ""
    pig_lab = text.split()

    for word in pig_lab:
        if word.isalpha():
            word = f'{word[1:]}{word[0]}ay '
            pig_latin += word
        else:
            pig_latin += word

    return pig_latin.rstrip()


test1 = pig_it('Pig latin is cool')
test2 = pig_it('Hello world !')
test3 = pig_it("Quis custodiet ipsos custodes ?")

print(test1)
print(test2)
print(test3)
