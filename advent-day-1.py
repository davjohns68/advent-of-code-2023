inputFile = open("/Users/djohnson/git/advent-of-code-2023/input-day-1.txt", "r")
calibrationLines = []
calibrationValues = []
for item in inputFile:
    calibrationLines.append(item)

# Part 1
for line in calibrationLines:
    firstDigit = ""
    lastDigit = ""
    combinedDigits = ""
    for character in line:
        if character.isdigit():
            if firstDigit == "":
                firstDigit = character
                lastDigit = character
            else:
                lastDigit = character
    combinedDigits = firstDigit + lastDigit
    calibrationValues.append(int(combinedDigits))
print(sum(calibrationValues))

# Part 2
def findDigit(subStr):
    if subStr.startswith("one"):
        return "1"
    elif subStr.startswith("two"):
        return "2"
    elif subStr.startswith("three"):
        return "3"
    elif subStr.startswith("four"):
        return "4"
    elif subStr.startswith("five"):
        return "5"
    elif subStr.startswith("six"):
        return "6"
    elif subStr.startswith("seven"):
        return "7"
    elif subStr.startswith("eight"):
        return "8"
    elif subStr.startswith("nine"):
        return "9"
    else:
        pass

calibrationValues = []
for line in calibrationLines:
    firstDigit = ""
    lastDigit = ""
    combinedDigits = ""
    for i in range(len(line)-1):
        if line[i].isdigit():
            if firstDigit == "":
                firstDigit = line[i]
                lastDigit = line[i]
            else:
                lastDigit = line[i]
        else:
            tempDigit = findDigit(line[i:])
            if tempDigit == None:
                continue
            if tempDigit.isdigit():
                if firstDigit == "":
                    firstDigit = tempDigit
                    lastDigit = tempDigit
                else:
                    lastDigit = tempDigit
    combinedDigits = firstDigit + lastDigit
    calibrationValues.append(int(combinedDigits))
print(sum(calibrationValues))

