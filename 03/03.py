with open("input.txt") as file:
    rucksacks = [line.strip() for line in file]


def findCommonLetter(sack: str):
    first_sack = sack[0:(int(len(sack)/2))]
    second_sack = sack[(int(len(sack)/2)):]
    print(first_sack+":"+second_sack)
    common_letter = None
    for first_letter in first_sack:
        for second_letter in second_sack:
            if second_letter == first_letter:
                common_letter = second_letter
                break
    print(common_letter)
    return common_letter


def findIDCard(sacks: list[str]):
    elf = 1
    score = 0
    temp_sack = ''
    for index, sack in enumerate(sacks):
        match elf:
            case 1:
                temp_sack = ''.join(set(sack).intersection(sacks[index+1]))
                elf = elf + 1
            case 2:
                common_letter = ''.join(set(temp_sack).intersection(sacks[index+1]))
                score = score + findScoreCard(common_letter)
                elf = elf + 1
            case 3:
                elf = 1
    return score


def findScoreCard(letter: str):
    score = 0
    if letter.islower():
        score = score + ord(letter)-96
    else:
        score = score + ord(letter)-38
    return score


def findScore(sacks: list):
    score = 0
    for sack in sacks:
        common_letter = findCommonLetter(sack)
        if common_letter.islower():
            score = score + ord(common_letter)-96
        else:
            score = score + ord(common_letter)-38
    return score

# solution 1
# print(findScore(rucksacks))

# solution 2
print(findIDCard(rucksacks))