import re


def to_camel_case(text):
    words = re.sub('[\W_]', "", text.title())
    return text[:1] + words[1:]

