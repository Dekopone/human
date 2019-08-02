# encoding utf-
import random


def hangman(word):
    wrong = 0
    stages = ["",
              "_____________     ",
              "|                 ",
              "|       |         ",
              "|       |         ",
              "|       0         ",
              "|      /|\        ",
              "|       |         ",
              "|       /\        ",
              "|"]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HangMan!!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess a character : "
        char = input(msg)
        if char in rletters:
            while char in rletters:
                cidx = rletters.index(char)
                board[cidx] = char
                rletters[cidx] = '$'
        else:
            wrong += 1
        print("  ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print("  ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("you Lose! The answer is \"{}\" .".format(word))


wordlist = ["beer", "jin", "chasis", "wotoka"]
rnum = random.randint(0, 3)
hangman(wordlist[rnum])
