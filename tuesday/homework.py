def hw(start, n):
    result = []
    for i in range(start, start+n*2):
        if i % 2 == 0:
            result.append(i)
        else:
            continue
    return result

print(hw(5, 7))
