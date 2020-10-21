#TODO
# DONE  convert to lists or array
# DONE  determine outcome from lists or array - functions x_win, o_win, empty_present, x_o_differences needs a bool <= 2
#figure how to organize data to test for completness or invalidity

#NOTE
# "Game not finished" when no side has a three in a row but there are still empty cells;
#  x_win:False, o_win:False, _present:True
# "Draw" when no side has a three in a row and there are no empty cells left;
# x_win:False, o_win:False, _present:False
# "X wins" when the field has three Xs in a row;
#  x_win:True, o_win:False, _present:False
# "O wins" when the field has three Os in a row;
#  x_win:False, o_win:True, _present:False
# "Impossible" when the field has three Xs in a row as well as three Os in a row. Or the field has a lot more Xs that Os or vice versa (if the difference is 2 or more, should be 1 or 0). For this stage, consider that the game can start both with X or O.
# x_win:True, o_win:True or |count_x - count_o| >= 2

# input = str(input()) # for submission
input = 'XXXOOXOXO' #NOTE change to input() see above

#Full string as individual string characters
input_parser = []

for char in input:
    input_parser.append(char)

#Rows, columns, and diagnonals outcomes as a list with each element as a three letter string i.e. 'XXX' or 'XOO'
outcomes = [
    input[0:3],     #row 1
    input[3:6],     #row 2
    input[6:9],     #row 3
    input[0::3],    #column 1
    input[1::3],    #column 2
    input[2::3],    #column 3
    input[::4],     #diagonal 1
    input[2:7:2]    #diagonal 2
]


# determines if x wins
for i in range(len(outcomes)):
    if outcomes[i] == 'XXX':
        x_win = True
    else:
        x_win = False

# determines if o wins
for i in range(len(outcomes)):
    if outcomes[i] == 'OOO':
        o_win = True
    else:
        o_win = False

# determines if there are emtpy spaces
for x in input:
    if x == '_' or x == ' ':
        empty_present = True
    else:
        empty_present = False


x_o_differences = abs(input_parser.count('X') - input_parser.count('O'))

# Printing output
print('---------')
print('|', input[0], input[1], input[2], '|')
print('|', input[3], input[4], input[5], '|')
print('|', input[6], input[7], input[8], '|')
print('---------')


# Data flow control
if x_win == False and o_win == False and empty_present == True:
    print('Game not finished')
elif x_win == False and o_win == False and empty_present == False:
    print('Draw')
elif x_win == True and o_win == False and empty_present == False:
    print('X wins')
elif x_win == False and o_win == True and empty_present == False:
    print('O wins')
elif (x_win == True and o_win == True) or (x_o_differences >= 2):
    print('Impossible')
else:
    print('Error')