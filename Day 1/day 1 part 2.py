file_contents = []

forward = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
backward = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}

with open('input.txt', 'r') as file:
    for line in file:
        file_contents.append(line.strip())

total = 0


def located_word(word):
    string = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'eno', 'owt', 'eerht', 'ruof',
              'evif', 'xis', 'neves', 'thgie', 'enin')
    for digit in string:
        if digit in word:
            return True
    return False


def extract_digits(word):
    for f_element, b_element in zip(forward, backward):
        if f_element in word:
            return forward[f_element]
        if b_element in word:
            return backward[b_element]



for line in file_contents:
    left, right = 0, len(line) - 1
    increment_left, increment_right = True, True
    word_left, word_right = "", ""

    while left < right and (increment_left or increment_right):

        if increment_left:
            word_left += line[left]
        if increment_right:
            word_right += line[right]

        if line[left].isdigit() or located_word(word_left):
            increment_left = False
        if line[right].isdigit() or located_word(word_right):
            increment_right = False

        if increment_left:
            left += 1
        elif increment_right:
            right -= 1

    if line[left].isdigit() and line[right].isdigit():
        number = line[left] + line[right]
        number = int(number)
        total += number
    elif not line[left].isdigit() and not line[right].isdigit():
        left_digit, right_digit = extract_digits(word_left), extract_digits(word_right)
        number = left_digit + right_digit
        number = int(number)
        total += number
    elif line[left].isdigit() and not line[right].isdigit():
        right_digit = extract_digits(word_right)
        number = line[left] + right_digit
        number = int(number)
        total += number
    elif not line[left].isdigit() and line[right].isdigit():
        left_digit = extract_digits(word_left)
        number = left_digit + line[right]
        number = int(number)
        total += number


print(total)
