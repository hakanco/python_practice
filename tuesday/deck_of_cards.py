import random

deck = []
for i in range(52):
    deck.append(i)


def shuffle(list_shuffle):
    for i in len(list_shuffle):
        j = random.randint(0, i)
        list_shuffle[i], list_shuffle[j] = list_shuffle[j], list_shuffle[i]
    return list_shuffle


