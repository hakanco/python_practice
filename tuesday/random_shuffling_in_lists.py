import random

values = []
for i in range(0,5):
    values.append(i)

for i in range(5):
    j = random.randint(0, i)
    # swap values
    values[i], values[j] = values[j], values[i]

print(values)