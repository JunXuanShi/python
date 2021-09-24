import random


def main():
    score = take_in_scores()
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")

        if 50 <= score <= 90:
            print("Passable and your score is {}".format(score))
        if score > 90:
            print("Excellent and your score is {}".format(score))
        if score < 50:
            print("Bad and your score is {}".format(score))


def take_in_scores():
    score = random.randint(0, 100)
    return score


main()
