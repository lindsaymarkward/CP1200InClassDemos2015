"""
In-class exercise,
"""
__author__ = 'sci-lmw1'

MASTER_SCORE = 100
KNIGHT_SCORE = 50


def main():
    countRounds = 0
    score = int(input("Score: "))

    while score < MASTER_SCORE:
        print("Your rank is", determineJediRank(score))
        scoreIncrement = int(input("Increment: "))
        score += scoreIncrement
        countRounds += 1

    print("Congratulations, Master!")
    print("That took you", countRounds, "rounds")


def determineJediRank(score):
    if score >= MASTER_SCORE:
        return "Master"
    elif score > KNIGHT_SCORE:
        return "Knight"
    else:
        return "Paduan"


main()