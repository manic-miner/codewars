def remove_consecutive_duplicates(s):
    words = s.split()
    result = [words[0]]

    for word in words:
        if word != result[-1]:
            result.append(word)

    return " ".join(words for words in result)