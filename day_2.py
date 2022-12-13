############### PART 1

labels = {
    'A': ('Rock', 1),
    'B': ('Paper', 2),
    'C': ('Scissors', 3),
    'X': ('Rock', 1),
    'Y': ('Paper', 2),
    'Z': ('Scissors', 3),
}
scoring = {
    'lose': 0,
    'draw': 3,
    'win': 6,
}
strat_guide = [
    ('A', 'Y'),
    ('B', 'X'),
    ('C', 'Z')
]

def determineVictorScore(val1, val2):
    """
    Determines if val1 wins in a game of Rock/Paper/Scissors
    :param val1:
    :param val2:
    :return: 'draw', 'lose', 'win'
    """
    score = 0
    result = None
    score += labels[val1][1]
    v1 = labels[val1][0]
    v2 = labels[val2][0]
    if v1 == v2:
        result = 'draw'
    elif (v1 == 'Rock' and v2 == 'Scissors') or (v1 == 'Scissors' and v2 == 'Paper') or (v1 == 'Paper' and v2 == 'Rock'):
        result = 'win'
    elif (v1 == 'Scissors' and v2 == 'Rock') or (v1 == 'Paper' and v2 == 'Scissors') or (v1 == 'Rock' and v2 == 'Paper'):
        result = 'lose'
    score += scoring[result]
    return score

score = 0
for opp, me in strat_guide:
    score += determineVictorScore(me, opp)
    print(determineVictorScore(me, opp))
print('---------')
print(score)

score = 0
file = 'strat_guide.txt'
with open(file, 'r') as file:
    for line in file.readlines():
        opp, me = line.split()
        score += determineVictorScore(me, opp)
print(score)

################## PART 2

labels = {
    'A': ('Rock', 1),
    'B': ('Paper', 2),
    'C': ('Scissors', 3),
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

def determineVictorScore2(val1, val2):
    """
    Determines the score for the round
    :param val1:
    :param val2:
    :return: 'draw', 'lose', 'win'
    """
    score = 0
    score += scoring[labels[val2]]
    v1 = labels[val1][0]
    v2 = labels[val2]
    if v2 == 'draw':
        score += labels[val1][1]
    elif (v2 == 'lose' and v1 == 'Rock') or (v2 == 'win' and v1 == 'Paper'):
        score += 3
    elif (v2 == 'lose' and v1 == 'Paper') or (v2 == 'win' and v1 == 'Scissors'):
        score += 1
    elif (v2 == 'lose' and v1 == 'Scissors') or (v2 == 'win' and v1 == 'Rock'):
        score += 2
    return score

score = 0
for opp, res in strat_guide:
    score += determineVictorScore2(opp, res)
    print(determineVictorScore2(opp, res))
print('---------')
print(score)

score = 0
file = 'strat_guide.txt'
with open(file, 'r') as file:
    for line in file.readlines():
        opp, res = line.split()
        score += determineVictorScore2(opp, res)
print(score)
