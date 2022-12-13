############### TEST LIST
strat_guide = [
    ('A', 'Y'),
    ('B', 'X'),
    ('C', 'Z')
]

############### PART 1
labels = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

def determineResult(rnd):
    """
    Determines if FIRST argument in rnd wins in a game of Rock/Paper/Scissors
    :param tup rnd: two competing entries (me, opp)
    :return: 'draw', 'lose', 'win'
    """
    wins = {
        ('Rock', 'Scissors'),
        ('Paper', 'Rock'),
        ('Scissors', 'Paper'),
    }
    losses = {
        ('Scissors', 'Rock'),
        ('Rock', 'Paper'),
        ('Paper', 'Scissors'),
    }
    rnd = (labels[rnd[0]], labels[rnd[1]])
    if rnd[0] == rnd[1]:
        return 'draw'
    elif rnd in wins:
        return 'win'
    elif rnd in losses:
        return 'lose'

def determineScore(res, rnd):
    """
    Determines the scoring for a round of Rock/Paper/Scissors
    :param str res: 'draw', 'win', 'lose'
    :param tup rnd: two competing entries (me, opp)
    :return: score
    """
    scoring = {
        'lose': 0,
        'draw': 3,
        'win': 6,
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
    }
    score = 0
    score += scoring[labels[rnd[1]]]
    score += scoring[res]
    return score

print('~~~~~ PART 1 ~~~~~')
print('-----PRACTICE-----')
score = 0
for round in strat_guide:
    score += determineScore(determineResult(tuple(reversed(round))), round)
    print(determineScore(determineResult(tuple(reversed(round))), round))
print(score)

print('-----FILE-----')
score = 0
file = 'strat_guide.txt'
with open(file, 'r') as file:
    for line in file.readlines():
        round = tuple(line.split())
        score += determineScore(determineResult(tuple(reversed(round))), round)
print(score)

################## PART 2
labels = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

def determineScore2(rnd):
    """
    Determines the scoring for a round of Rock/Paper/Scissors
    :param tup rnd: opponents entry and desired result
    :return: score
    """
    scoring = {
        'lose': 0,
        'draw': 3,
        'win': 6,
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
    }
    losses = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper',
    }
    wins = {
        'Scissors': 'Rock',
        'Rock': 'Paper',
        'Paper': 'Scissors',
    }
    score = 0
    score += scoring[labels[rnd[1]]]
    if labels[rnd[1]] == 'draw':
        score += scoring[labels[rnd[0]]]
    elif labels[rnd[1]] == 'win':
        score += scoring[wins[labels[rnd[0]]]]
    elif labels[rnd[1]] == 'lose':
        score += scoring[losses[labels[rnd[0]]]]
    return score

print('~~~~~ PART 2 ~~~~~')
print('-----PRACTICE-----')
score = 0
for round in strat_guide:
    score += determineScore2(round)
    print(determineScore2(round))
print(score)

print('-----FILE-----')
score = 0
file = 'strat_guide.txt'
with open(file, 'r') as file:
    for line in file.readlines():
        round = tuple(line.split())
        score += determineScore2(round)
print(score)
