def remove_consecutive_duplicates(s):
    words = s.split()
    if len(words) > 0:
        result = [words[0]]
    else:
        return ""

    for word in words:
        if word != result[-1]:
            result.append(word)

    return " ".join(words for words in result)