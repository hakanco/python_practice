import random

numbers = []
for i in range(100):
    numbers.append(random.randint(0, 100))

avg_number = sum(numbers) / len(numbers)

count = 0
for i in numbers:
    if i > avg_number:
        count += 1
print(f'Average of those integers is {avg_number} and {count} of them are above the average.')
