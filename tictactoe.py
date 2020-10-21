#TODO
# DONE  convert to lists or array
# DONE  determine outcome from lists or array - functions x_win, o_win, empty_present, x_o_diff needs a bool <= 2
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
input_parser = []

for char in input:
    input_parser.append(char)

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


def x_win():
    for i in range(len(outcomes)):
        print(outcomes[i])
    if outcomes[x] == 'XXX':
        print('X wins')
        return True
    else:
        return False

def o_win():
    for i in range(len(outcomes)):
        print(outcomes[i])
    if outcomes[i] == 'OOO':
        print('O win')
        return True
    else:
        return False

def empty_present():
    for x in input:
        if x == '_' or x == ' ':
            print('Has unfilled slots')
            return True
        else:
            return False

def x_o_diff():
    difference = abs(input_parser.count('X') - input_parser.count('O'))
    return difference

print('spaces present :', empty_present())
print('differences between x o count :', x_o_diff())