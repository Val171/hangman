import hangman_resources
import random
import os
print(hangman_resources.logo)
lives = 6
word = random.choice(hangman_resources.word_list)
wo_list = list(word)

X = []

for i in wo_list:
    X += "_"
print("".join(X))
print()

while "_" in X:
    guess = input("Guess a letter: ").lower()
    if guess in X:
        print("You've already guessed that dumbass")
    for i in range(len(wo_list)):
        letter = wo_list[i]
        if letter == guess:
            X[i] = letter
            print(hangman_resources.list_lives[lives])
        if guess not in word:
            lives -= 1
            print(hangman_resources.list_lives[lives])
            print(f"{guess} is not in the word, lost a life, oops.")
            print()
            break
    if lives == 0:
        print(hangman_resources.lose)
        break
    print("".join(X))
if lives != 0:
    print(hangman_resources.win)






