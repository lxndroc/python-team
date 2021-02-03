'''
+ Build Your Dream Python Project (BYDPP) +
Team Invite: https://dsc.gg/python_team
BYDPP 2021 Coaching Call #02 (BYDPP21CC02) +
1 Feb 2021, 8pm GMT
Host: @Mircea
Coach: @alexandros
Task Reference
 Gaddis T., Starting Out with Python, Pearson, 2019, 4th global ed.
 p306 Programming Exercise 21

Task
21. Rock, Paper, Scissors Game

Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
The program should work as follows.
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. 
If the number is 2, then the computer has chosen paper. 
If the number is 3, then the computer has chosen scissors.
(Don't display the computer's choice yet.)
2. The user enters his or her choice of "rock", "paper", or "scissors" at the keyboard.
3. The computer's choice is displayed.
4. A winner is selected according to the following rules:
   • If one player chooses rock and the other player chooses scissors, then rock wins.
(The rock smashes the scissors.)
   • If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
   • If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
   • If both players make the same choice, the game must be played again to determine the winner.

Python Code
As below, being non-optimised, as in the call.
'''

import random

def main():
    display_menu()
    c, m = get_choices()
    display_moves(c, m)

def display_moves(c, m):
    while m > 3:
        m = int(input('Please print appropriate number: '))
    if m == 1 and c == 2:
        print('You moved rock and computer moved paper\n'
              'Paper wraps rock.\n'
              'Computer wins!')
    elif m == 1 and c == 3:
        print('You moved rock and computer moved scissors\n'
              'Rock smashes scissors.\n'
              'You win!')
    elif m == 2 and c == 1:
        print('You moved paper and computer moved rock\n'
              'Paper wraps rock.\n'
              'You win!')
    elif m == 2 and c == 3:
        print('You moved paper and computer moved scissors\n'
              'Scissors cuts paper.\n'
              'Computer wins!')
    elif m == 3 and c == 2:
        print('You moved scissors and computer moved paper\n'
              'Scissors cuts paper.\n'
              'You win!')
    elif m == 3 and c == 1:
        print("You moved scissors and computer moved rock\n"
              "Rock smashes scissors.\n"
              "Computer wins!")
    else:
        print('You both selected the same.\n'
              'It is a tie.\n'
              'Try again.')
        c, m = get_choices()
        display_moves(c, m)

def get_choices():
    m = int(input('Please enter your choice: '))
    c = random.randrange(1, 4)
    return c, m

def display_menu():
    print('\t Menu\n'
          '1) Rock\n'
          '2) Paper\n'
          '3) Scissors')

main()