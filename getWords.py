from bigdict import Dictionary
with open('fiveLetterWords.txt', 'w') as res:
    for word in Dictionary:
        if len(word) == 5:
            res.write(word+"\n")

with open('wordlist10000.txt', 'r') as wor:
    with open('solutionwords.txt', 'w') as res:
        for line in wor:
            if(len(line)==6) and line[:-1] in Dictionary:
                res.write(line)
