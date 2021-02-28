'''
+Build Your Dream Python Project Discord Team
Invite: https://dsc.gg/python_team
19 Feb 2021
@alexandros answer to @Subham
https://discord.com/channels/794684213697052712/794684213697052718/812231193213796362
Sublist Yielder
'''

lst = [[1, 3, 4], [2, 5, 7]]
 
def f(lst):
    for sublst in lst:
        yield from sublst
        yield '\n'
          
for item in f(lst):
    end_char = '' if item == '\n' else ' '
    print(item, end = end_char)

# Output
'''
1 3 4 
2 5 7 
'''
