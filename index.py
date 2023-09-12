# import random
# l = ["rock","paper","sessior"]
# userPoint = 0
# compPoint = 0
# while True:
#     # userInput = int(input(''' 
#     #     1 START GAME 
#     #     2 EXIT GAME
#     #     '''))
#     # if userInput == 1:
#     for i in range(6):
#          gameInput = int(input('''
#         1 ROCK
#         2 PAPER 
#         3 SESSIOR
#          '''))
#          compInp = random.choice(l)
#          if gameInput == 1:
#             userChoic = l[0]
#          elif gameInput == 2:
#             userChoic = l[1]
#          elif gameInput == 3:
#             userChoic = l[2]
        
#          if (userChoic == "rock" and compInp == "sessior") or (userChoic == "sessior" and compInp == "paper") or (userChoic == "paper" and compInp == "rock"):
#             userPoint = userPoint + 1
#             print("user won the match")
#             print("user choice is : ",userChoic)
#             print("computer choice is : ",compInp)
#             print("TOTAL USER POINT : ",userPoint, " TOTAL COMPUTER POINT ",compPoint)
#          elif (userChoic == "rock" and compInp == "rock") or (userChoic == "sessior" and compInp == "sessior") or (userChoic == "paper" and compInp == "paper"):
#             print("mathch draw")
#             print("TOTAL USER POINT : ",userPoint, " TOTAL COMPUTER POINT ",compPoint)
#          else:
#             compPoint = compPoint + 1
#             print("computer won the game ")
#             print("user choice is : ")
#             print("computer choice is : ",compInp)
#             print("TOTAL USER POINT : ",userPoint, " TOTAL COMPUTER POINT ",compPoint)
#             break
# if userPoint > compPoint:
#     print("user won the game")
# elif userPoint == compPoint:
#     print("match draw")
# else:
#     print("computer won the game")

import random

l = ["rock", "paper", "scissor"]
userPoint = 0
compPoint = 0
rounds = 6  # Adjust the number of rounds as needed

for _ in range(rounds):
    gameInput = int(input('''
    1 ROCK
    2 PAPER 
    3 SCISSOR
     '''))
    compInp = random.choice(l)

    if gameInput == 1:
        userChoic = l[0]
    elif gameInput == 2:
        userChoic = l[1]
    elif gameInput == 3:
        userChoic = l[2]

    if (userChoic == "rock" and compInp == "scissor") or (userChoic == "scissor" and compInp == "paper") or (userChoic == "paper" and compInp == "rock"):
        userPoint += 1
        print("User won the match")
    elif (userChoic == "rock" and compInp == "rock") or (userChoic == "scissor" and compInp == "scissor") or (userChoic == "paper" and compInp == "paper"):
        print("Match draw")
    else:
        compPoint += 1
        print("Computer won the game")

print("Total User Points:", userPoint)
print("Total Computer Points:", compPoint)

if userPoint > compPoint:
    print("User won the game")
elif userPoint == compPoint:
    print("Match draw")
else:
    print("Computer won the game")
