file_contents = []

with open('input.txt', 'r') as file:
    for line in file:
        file_contents.append(line.strip())

total = 0

for line in file_contents:
    left, right = 0, len(line) - 1
    while left < right and (not line[left].isdigit() or not line[right].isdigit()):
        if not line[left].isdigit():
            left += 1
        if not line[right].isdigit():
            right -= 1
    number = line[left] + line[right]
    number = int(number)
    total += number

print(total)
