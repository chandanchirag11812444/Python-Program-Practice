#the game function in a program lets a user play a game and returns the score as an integer.
#you need to read file 'hiscore.txt'which is either blank or contains the previous hi-score
#you need to write a program to update the high-score whenever game() breaks the hi-score.


def game():
    return 568



score=game()

with open('hiscore.txt') as f:
    hiscorestr=f.read()
if hiscorestr=='':
    with open('hiscore.txt','w') as f:
        f.write(str(score))

elif int(hiscorestr)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))
                