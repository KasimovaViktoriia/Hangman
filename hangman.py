import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman!\n")

    while wrong < len(stages) - 1:
        char = input("Guess a letter: ")
        if char in remaining_letters:
            char_index = remaining_letters.index(char)
            board[char_index] = char
            remaining_letters[char_index] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        cur_stage = wrong + 1
        print("\n".join(stages[0: cur_stage]) + "\n")

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print(f"You lose! It was {word}.")

words = ["cat", "dog", "turtle", "parrot", "snake", "cow", "lamb", "chicken"]
word = random.choice(words)
hangman(word)
