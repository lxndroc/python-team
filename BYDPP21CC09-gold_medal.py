'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #09 (BYDPP21CC09)
5 Mar 2021, 8pm GMT
Host: @Mk
Coach: @alexandros
 
Task
Gold medal
Write a game that allows two players to play Blackjack.
The rules of the game are simple.
Each player is given a random starting card.
Players then take turns to "stick" or "twist".
If they "twist", they are given another (random) card
and then it becomes their opponent's turn.
The opponents also choose "stick" or "twist"
and have the choice to draw a card or not.
Players take turns receiving cards until one of them "sticks".
At this point that player receives no more cards.
The other player can carry on "twisting" if they choose,
and can keep doing so until they too "stick".
The objective of the game is to get the highest possible points value
of their cards without going above the value of 21.
If a player twists and their total goes over 21, they lose the game.
If both players choose to stick without going over 21,
the winner is the player who has the highest points value
when all their cards are added.
Don't forget that an Ace can be counted as EITHER 1 or 11!

Python Code - Initial Effort
As below, being non-optimised, as in the call with minor edits.
'''

import random

rdict = {
  "Ace": 1,
  "Two": 2,
  "Three": 3,
  "Four": 4,
  "Five": 5
}

test = [1,2,3,4]

test2 = ["Ace", "TWo", "three"]

num = random.choice(list(rdict.keys()))
print("Your card is :",num)
points = 0
drawn = []

while True:
    print()
    guess = input("higher or lower:  ")
    rdm = random.choice([i for i in rdict.keys() if i not in drawn])
    drawn.append(rdm)
#    print(drawn)
    if guess == "lower" and rdict[rdm] < rdict[num]:
        print("You got: ", rdm)
        points = points +1
        print("Points: ", points)
    elif guess == "lower" and rdict[rdm] > rdict[num]:
        print("You got: ", rdm)
        print("You lost.")
        print("Your score: ", points)
        break
    elif guess == "higher" and rdict[rdm] > rdict[num]:
        print("You got: ", rdm)
        points = points + 1
        print("Points: ", points)
    elif guess == "higher" and rdict[rdm] < rdict[num]:
        print("You got: ", rdm)
        print("You lost.")
        print("Your score: ", points)
        break
