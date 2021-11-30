
def find_chinese_zodiac():
    year = int(input("Please enter a year!\n"))
    remainder = (year % 12)
    switcher = {
        0: 'monkey',
        1: 'rooster',
        2: 'dog',
        3: 'pig',
        4: 'rat',
        5: 'ox',
        6: 'tiger',
        7: 'rabbit',
        8: 'dragon',
        9: 'snake',
        10: 'horse',
        11: 'sheep'
    }
    return switcher.get(remainder, "none of them")


print(f"Animal of the year that you entered is {find_chinese_zodiac()}.")
