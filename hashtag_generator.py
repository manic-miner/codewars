def generate_hashtag(s):
    output = "#" + "".join(s.title().replace(" ", "").strip())
    return False if (len(s) <= 0 or len(output) > 140) else output

