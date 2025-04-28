import random

NUM_SIDES = 6


def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)


def main():
    die1 = 10
    print(f"{die1} in main() start as {die1}")

    for _ in range(3):
        roll_dice()
        print(f"{die1} in main() still {die1}")


if __name__ == '__main__':
    main()
