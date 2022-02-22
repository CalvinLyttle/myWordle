import random

f = open("fiveLetterWords.txt", "r")
fiveLetterWords = f.readlines()
f.close()
#print("about\n" in fiveLetterWords)

s = open("solutionwords.txt", "r")
solutions = s.readlines()
s.close()

NUMLETTERS = 5
while True:
    abcd = "abcdefghijklmnopqrstuvwxyz"
    abcLi = list(abcd)
    word = random.choice(solutions)
    i = 0
    while True:
        if i == 6:
            print("Sorry, you lose. The word was %s." % word)
            break
        if not i:
            guess = input("Input a %s letter word:\n" % NUMLETTERS)
        else:
            guess = input("")
        guess = guess + "\n"
        i += 1
        if not (guess in fiveLetterWords or guess in solutions):
            print("Not in word list")
            i -= 1
            continue
        if guess == word:
            print("You win!")
            break
        show = ""
        for j in range(NUMLETTERS):
            if guess[j] == word[j]:
                show += "g"
            elif guess[j] in word:
                show += "y"
            else:
                show += "b"
                if (guess[j] in abcLi): abcLi.remove(guess[j])
        print(show + "\n")
        print("Remaining letters: %s \n" % abcLi)
    playAgain = input("Would you like to play again? Y/N: ")
    if playAgain == "N" or playAgain == "n":
        break