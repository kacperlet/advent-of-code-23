import re

colors = [("red", 12), ("green", 13), ("blue", 14)]
gamePattern = "(?!(Game))[0-9]+"

sumID = 0 # sum of possible game IDs
sumPowers = 0
with open("day2.txt", 'r') as file:
    f = file.readlines()
    for line in f:
        game = int(re.search(gamePattern, line).group())
        possible = True
        power = 1
        for i in range(3):
            searchPattern = f'[0-9]+(?=( {colors[i][0]}))'
            colorMax = 0
            for m in re.finditer(searchPattern, line):
                num = int(m.group())
                if (num > colors[i][1]):
                    possible = False
                if (num > colorMax):
                    colorMax = num
            power *= colorMax
        if (possible):
            sumID += game
        sumPowers += power

print("Sum of games where it is possible:", sumID) #2551
print("Sum of powers:", sumPowers) #62811

