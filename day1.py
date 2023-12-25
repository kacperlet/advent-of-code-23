import re
nums = "|".join("one two three four five six seven eight nine".split(" "))
pattern = "(?=([0-9]|" +nums+ "))"
print(pattern)

toInt = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1":"1", # quicker to do this then just check
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

total = 0
with open("day1.txt", 'r') as file:
    f = file.readlines()
    for line in f:
        matches = re.findall(pattern, line)
        total += int(toInt[matches[0]] + toInt[matches[-1]])
        print(line[0: -1], matches, int(toInt[matches[0]] + toInt[matches[-1]]))

    
print(total)
