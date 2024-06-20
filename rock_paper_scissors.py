# start the game
print("game start")

#ask player to insert a move R for Rock p for paper S for scissors
userInsert = input("choose your move 'r' for Rock , 'p' for paper, 's' for scissors ?")

#computer will choose randomly 
import random

pcInsert = random.choice(['r', 'p' , 's'])

print(f'user choosed {userInsert}')
print(f'pc choosed {pcInsert}')

if userInsert == pcInsert:
    print("its a tie")
elif userInsert == 'r' and pcInsert == 's' or userInsert == 's' and pcInsert == 'p' or userInsert == 'p' and pcInsert == 'r':
    print('You are the winner')
else:
    print('You lost')

