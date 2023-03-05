from collections import Counter


def top_3_words(text):
    frequency = {}
    for word in text.lower().split():
        if word in frequency.keys():
            frequency[word] += 1
        else:
            frequency[word] = 1

    count = Counter(frequency)
    top_3 = count.most_common(3)
    result = []
    for i in top_3:
        result.append(i[0])

    return result


test1 = top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]
print(test1)
