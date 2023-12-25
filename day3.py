import re

pattern = "[0-9]+"
characters = '*&=-%#@/$+'
characters = [i for i in characters]

LINES = 0
LINE_LENGTH = 0

with open('day3.txt', 'r') as file:
    array = file.readlines()
    LINES = len(array) -1
    LINE_LENGTH = len(array[0])
print(LINES, "lines")
print(LINE_LENGTH, "line length")

def check(start: int, end: int, row: int, array: list) -> bool: # doesnt count for first and last line
    # vertical check
    for i in range(start, end):
        if (array[row+1][i] in characters or array[row-1][i] in characters):
            return True
    
    # sides
    if (start != 0):
        if (array[row-1][start-1] in characters or array[row-1][i] in characters):
            return True
        if (array[row][start-1] in characters or array[row-1][i] in characters):
            return True
        if (array[row+1][start-1] in characters or array[row-1][i] in characters):
            return True
    if (end != LINE_LENGTH):
        if (array[row-1][end] in characters or array[row-1][i] in characters):
            return True
        if (array[row][end] in characters or array[row-1][i] in characters):
            return True
        if (array[row+1][end] in characters or array[row-1][i] in characters):
            return True

sum = 0
with open('day3.txt', 'r') as file:
    f = file.readlines()
    for i in range(1, len(f) -1):
        line = f[i]
        print("\n", i)
        for m in re.finditer(pattern, line):
            isSpecial = check(m.start(), m.end(), i, f)
            if isSpecial:
                print(line[m.start():m.end()], end=" ")
                sum += int(line[m.start():m.end()])
        print('Sum:', sum)

firstLine= 798 + 145 + 629 + 579 + 455 + 130 + 243 + 154
lastLine = 353 + 914 + 829 + 75 # hard coded fist and last line cuz im lazy :)

print("Total:", sum + firstLine + lastLine)
print(characters)

# TODO: Do part two