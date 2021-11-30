values = [0, 1, 2, 3, 4]

# retain the first element
temp = values[0]

# shift elements left
for i in range(1, 5):
    values[i-1] = values[i]

# move the first element to fill the last position

values[len(values)-1] = temp

print(values)