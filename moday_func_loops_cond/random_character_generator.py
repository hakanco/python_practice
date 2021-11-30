import random


def r_c_g():
    return chr(random.randint(ord("a"), ord("z")))


print("{} letter is generated randomly.".format(r_c_g()))
