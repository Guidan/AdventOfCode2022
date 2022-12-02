ROCK_PAPER_SCISSORS_KEY = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

WIN = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

LOSE = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}


with open("input.txt") as file:
    strategy = [line.strip() for line in file]


# first half of puzzle function
def calculatePoints(round: str):
    opponent = round[0]
    player = round[2]
    score = 0
    match ROCK_PAPER_SCISSORS_KEY[player]:
        case 'ROCK':
            score = score + 1
        case 'PAPER':
            score = score + 2
        case 'SCISSORS':
            score = score + 3
    if ROCK_PAPER_SCISSORS_KEY[opponent] == ROCK_PAPER_SCISSORS_KEY[player]:
        score = score + 3
    elif ROCK_PAPER_SCISSORS_KEY[player] == 'ROCK':
        if ROCK_PAPER_SCISSORS_KEY[opponent] == 'SCISSORS':
            score = score + 6
    elif ROCK_PAPER_SCISSORS_KEY[player] == 'PAPER':
        if ROCK_PAPER_SCISSORS_KEY[opponent] == 'ROCK':
            score = score + 6
    elif ROCK_PAPER_SCISSORS_KEY[player] == 'SCISSORS':
        if ROCK_PAPER_SCISSORS_KEY[opponent] == 'PAPER':
            score = score + 6
    return score


# Second half of puzzle function
def calculateStrategy(round: str):
    opponent = round[0]
    choice = round[2]
    score = 0
    player = None
    if choice == 'Y':
        player = opponent
        score = score + 3
    elif choice == 'X':
        player = LOSE[opponent]
    elif choice == 'Z':
        player = WIN[opponent]
        score = score + 6
    match ROCK_PAPER_SCISSORS_KEY[player]:
        case 'ROCK':
            score = score + 1
        case 'PAPER':
            score = score + 2
        case 'SCISSORS':
            score = score + 3
    return score


def getTotalScore(guide: list):
    total_score = 0
    for game in guide:
        # uncomment line 81 for part 1
        # total_score = total_score + calculatePoints(game)
        total_score = total_score + calculateStrategy(game)
    return total_score


print("The total score of the guide is {}".format(getTotalScore(strategy)))