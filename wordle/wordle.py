
from colorama import init,Back
import random
import string

def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

def checkinput(wrd,guess):
    strout=''
    for idx,i in enumerate(guess):
        if wrd[idx]==i:
            strout=strout + Back.GREEN + ' ' + i + ' '+ Back.BLACK + ' '
        elif i in wrd:
            strout=strout + Back.YELLOW + ' ' + i + ' '+ Back.BLACK + ' '
        else:
            strout=strout + Back.BLACK + ' ' + i + ' '+ Back.BLACK + ' '
            
    return strout

init(autoreset=True)
word= random_char(5)
word= 'azure'
loop =True
loopcount=0
win=False

print('I am ready with the word. Any guess?\n')

while(loop):
    loopcount+=1
    print('What is your guess?: ',end='')
    userinput = input()
    while (len(userinput) != 5):
        print('\033[1A',end='')
        print('What is your guess?: ',end='')
        userinput = input()
        
    if userinput=='exit!':
        break
    if userinput==word:
        win=True
        print('\033[{}C\033[1A'.format(23+len(userinput)) + '{} '.format(checkinput(word,userinput)))
        break
    print('\033[{}C\033[1A'.format(23+len(userinput)) + '{} '.format(checkinput(word,userinput)))
    
    if loopcount==6:
        loop=False


if(win):
    print('You Won !')
else:
    print('Better guess next time !')
    print('word was '+ word)

