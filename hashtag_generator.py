def generate_hashtag(s):
    if 0 < len(s) <= 140:
        return "#" + "".join(s.title().replace(" ", "").strip())
    else:
        return False

