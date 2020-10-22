#TODO
# The program should work in the following way:

# Get the 3x3 field from the input as in the previous stages.
# Output this 3x3 field with cells before the user's move.
# Then ask the user about his next move.
# Then the user should input 2 numbers that represent the coordinates of the cell which they want to mark X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input)
# Analyze user input and show these messages in the following situations:
# -"This cell is occupied! Choose another one!" if the cell is not empty;
# -"You should enter numbers!" if the user enters other symbols instead of numbers;
# -"Coordinates should be from 1 to 3!" if the user goes beyond the field.
# Then output the table including the user's most recent move.
# The program should also check user input. If it's unsuitable, the program should ask them to enter their coordinates once again.

# So, you need to output a field from the first line of the input and then ask the user to make their move. Keep asking until the user enters coordinates that represent an empty cell on the field and after that output the field with that move. You should output the field only 2 times, before and after a correct move.

# Do not delete code that checks table state; it will be useful in the future.


#NOTE
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
# Make a map between coordinates and locations

# input = str(input("Enter cells: ")) # for submission
print("Enter cells: ")
input = '_O_X__X_X' #NOTE change to input() see above


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
        print('X wins')
        break
    else:
        x_win = False

# determines if o wins
for i in range(len(outcomes)):
    if outcomes[i] == 'OOO':
        o_win = True
        break
    else:
        o_win = False

# determines if there are emtpy spaces
for x in input:
    if x == '_' or x == ' ':
        empty_present = True
        break
    else:
        empty_present = False


x_o_differences = abs(input_parser.count('X') - input_parser.count('O'))

# Printing test vars
# print('x wins :', x_win)
# print('o wins :', o_win)
# print('emp spaces :', empty_present)
# print('x o diff :', x_o_differences)
# Printing output
print('---------')
print('|', input[0], input[1], input[2], '|')
print('|', input[3], input[4], input[5], '|')
print('|', input[6], input[7], input[8], '|')
print('---------')


#--------------------------------------------------
print("Enter coords: ")
coords_x, coords_y = '3 1'.split(" ")
print(coords_x, coords_y)
print(type(coords_x))

# 0(1, 3) 1(2, 3) 2(3, 3)
# 3(1, 2) 4(2, 2) 5(3, 2)
# 6(1, 1) 7(2, 1) 8(3, 1)
def if_empty_repl(x, y):
    if input_parser[n] == ('_' or ' '):
        input_parser[n] = 'X'

if coords_x == '1':
    if coords_y == '1':
        print(input_parser[6])
    elif coords_y == '2':
        print(input_parser[3])
    elif coords_y == '3':
        print(input_parser[0])
elif coords_x == '2':
    if coords_y == '1':
        print(input_parser[7])
    elif coords_y == '2':
        print(input_parser[4])
    elif coords_y == '3':
        print(input_parser[1])
elif coords_x == '3':
    if coords_y == '1':
        print(input_parser[8])
    elif coords_y == '2':
        print(input_parser[5])
    elif coords_y == '3':
        print(input_parser[2])
else:
    print("Problem")
# if empty replace with x


# Data flow control
# if x_win == True and o_win == False:
#     print('X wins')
# elif x_win == False and o_win == True:
#     print('O wins')
# elif (x_win == True and o_win == True) or (x_o_differences >= 2):
#     print('Impossible')
#     repeat_this = True
# elif x_win == False and o_win == False and empty_present == False:
#     print('Draw')
# elif (x_win == False) and (o_win == False) and (empty_present == True):
#     print('Game not finished')
# else:
#     print('Error')
