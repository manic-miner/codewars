import math


def get_middle(s):
    return s[math.floor(len(s)/2)] if len(s) % 2 != 0 else s[round(len(s)/2-1)]+s[round(len(s)/2)]


#  late night solution :)
