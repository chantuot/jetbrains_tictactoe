#TODO
# The program should work in the following way:

# Get the 3x3 field from the og_board_state as in the previous stages.
# Output this 3x3 field with cells before the user's move.
# Then ask the user about his next move.
# Then the user should og_board_state 2 numbers that represent the coordinates of the cell which they want to mark X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user og_board_state)
# Analyze user og_board_state and show these messages in the following situations:
# -"This cell is occupied! Choose another one!" if the cell is not empty;
# -"You should enter numbers!" if the user enters other symbols instead of numbers;
# -"Coordinates should be from 1 to 3!" if the user goes beyond the field.
# Then output the table including the user's most recent move.
# The program should also check user og_board_state. If it's unsuitable, the program should ask them to enter their coordinates once again.

# So, you need to output a field from the first line of the og_board_state and then ask the user to make their move. Keep asking until the user enters coordinates that represent an empty cell on the field and after that output the field with that move. You should output the field only 2 times, before and after a correct move.

# Do not delete code that checks table state; it will be useful in the future.


#NOTE
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
# Make a map between coordinates and locations

# og_board_state = str(og_board_state("Enter cells: ")) # for submission
print("Enter cells: ")
og_board_state = '_O_X__X_X' #NOTE change to og_board_state() see above


#Full string as individual string characters
og_board_state_parser = []

for char in og_board_state:
    og_board_state_parser.append(char)

#Rows, columns, and diagnonals outcomes as a list with each element as a three letter string i.e. 'XXX' or 'XOO'
outcomes = [
    og_board_state[0:3],     #row 1
    og_board_state[3:6],     #row 2
    og_board_state[6:9],     #row 3
    og_board_state[0::3],    #column 1
    og_board_state[1::3],    #column 2
    og_board_state[2::3],    #column 3
    og_board_state[::4],     #diagonal 1
    og_board_state[2:7:2]    #diagonal 2
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
for x in og_board_state:
    if x == '_' or x == ' ':
        empty_present = True
        break
    else:
        empty_present = False


x_o_differences = abs(og_board_state_parser.count('X') - og_board_state_parser.count('O'))

# if empty replace with x
def if_empty_replace(n):
    if og_board_state_parser[n] == ('_' or ' '):
        og_board_state_parser[n] = 'X'
        print(og_board_state_parser[n])
    else:
        print('This cell is occupied! Choose another one!')
        if_empty_replace(n)

# Printing test vars
# print('x wins :', x_win)
# print('o wins :', o_win)
# print('emp spaces :', empty_present)
# print('x o diff :', x_o_differences)
# Printing output
print('---------')
print('|', og_board_state[0], og_board_state[1], og_board_state[2], '|')
print('|', og_board_state[3], og_board_state[4], og_board_state[5], '|')
print('|', og_board_state[6], og_board_state[7], og_board_state[8], '|')
print('---------')


#--------------------------------------------------
while True:
    try:
        print("Enter coords: ")
        # position = og_board_state()
        # position = position.split(" ")
        # print(position)
        coords_x, coords_y = input().split(" ")
        print(coords_x, coords_y)
        coords_x = int(coords_x)
        coords_y = int(coords_y)
        print('coords x:', type(coords_x), 'coords y:', type(coords_y))
        if coords_x == 1:
            if coords_y == 1:
                print(og_board_state_parser[6])
                if_empty_replace(6)
            elif coords_y == 2:
                print(og_board_state_parser[3])
                if_empty_replace(3)
            elif coords_y == 3:
                print(og_board_state_parser[0])
                if_empty_replace(0)
        elif coords_x == 2:
            if coords_y == 1:
                print(og_board_state_parser[7])
                if_empty_replace(7)
            elif coords_y == 2:
                print(og_board_state_parser[4])
                if_empty_replace(4)
            elif coords_y == 3:
                print(og_board_state_parser[1])
                if_empty_replace(1)
        elif coords_x == 3:
            if coords_y == 1:
                print(og_board_state_parser[8])
                if_empty_replace(8)
            elif coords_y == 2:
                print(og_board_state_parser[5])
                if_empty_replace(5)
            elif coords_y == 3:
                print(og_board_state_parser[2])
                if_empty_replace(2)
        elif coords_x < 1 or coords_x > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            print("Problem")
        break
    except ValueError:
        print("You should enter numbers")
        break

def coordinate_filters(coords_x, coords_y): # change function to convert to int afterwards
    if int(coords_x) == ValueError:
        print('yuh')
    elif coords_x != ('1' or '2' or '3'):
        print('You should enter numbers!')

print('---------')
print('|', og_board_state[0], og_board_state[1], og_board_state[2], '|')
print('|', og_board_state[3], og_board_state[4], og_board_state[5], '|')
print('|', og_board_state[6], og_board_state[7], og_board_state[8], '|')
print('---------')

# 0(1, 3) 1(2, 3) 2(3, 3)
# 3(1, 2) 4(2, 2) 5(3, 2)
# 6(1, 1) 7(2, 1) 8(3, 1)

# change below to function to replace coord with x or o
# determines coordinates and whats in the location

# if coords_x == 1:
#     if coords_y == 1:
#         print(og_board_state_parser[6])
#     elif coords_y == 2:
#         print(og_board_state_parser[3])
#     elif coords_y == 3:
#         print(og_board_state_parser[0])
# elif coords_x == 2:
#     if coords_y == 1:
#         print(og_board_state_parser[7])
#     elif coords_y == 2:
#         print(og_board_state_parser[4])
#     elif coords_y == 3:
#         print(og_board_state_parser[1])
# elif coords_x == 3:
#     if coords_y == 1:
#         print(og_board_state_parser[8])
#         if_empty_replace(8)
#     elif coords_y == 2:
#         print(og_board_state_parser[5])
#     elif coords_y == 3:
#         print(og_board_state_parser[2])
# # elif type(coords_x) != int:
# #     print('You should enter numbers!')
# elif coords_x < 1 or coords_x > 3:
#     print("Coordinates should be from 1 to 3!")
# else:
#     print("Problem")




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
#Helllo Channnnnnnn
