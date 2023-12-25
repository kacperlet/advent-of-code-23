import re

pattern = "[0-9]+"
sum = 0

with open("day4.txt", 'r') as file:
    f = file.readlines()

    startIndex = f[0].index(":") + 2
    endIndex = f[0].index("|")
    print(startIndex, endIndex)

    for i in range(len(f)):
        matches = 0
        winningNumbers = re.findall(pattern, f[i][startIndex: endIndex])
        numbersYouHave = re.findall(pattern, f[i][endIndex +1:])
        for num in winningNumbers:
            if num in numbersYouHave:
                matches += 1
        if (matches != 0):
            sum += 2**(matches-1)

print(sum)
    