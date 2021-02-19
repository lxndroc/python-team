'''
+Build Your Dream Python Project Discord Team
Invite: https://dsc.gg/python_team
19 Feb 2021
@alexandros answer to @CelestialTitania
Snailrun
'''

def snail_run(size=10):
    snail = "@>"
    for i in range(size):
        print("*" * size)
        if i < size - 1:
            print(' ' * i + snail + ' ' * (size - len(snail) - i) + '|')

snail_run_size = eval(input('Enter snail run size: '))
snail_run(snail_run_size)

# Sample Output
'''
Enter snail run size: 5
*****
@>   |
*****
 @>  |
*****
  @> |
*****
   @>|
*****
'''
