values = []
for i in range(1, 66, 5):
    values.append(i)

maxim = values[0]

for i in range(len(values)):
    if values[i] > maxim:
        maxim = values[i]

print(maxim)
