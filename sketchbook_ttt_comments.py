
def get_coords():
    print("Enter coords: ")
    global coords_x, coords_y
    coords_x, coords_y = input().split(" ")
    print(coords_x, coords_y)
    coords_x = int(coords_x)
    coords_y = int(coords_y)
    print('coords x:', type(coords_x), 'coords y:', type(coords_y))

# check cells to see if they are empty or not and replace with X or O if empty
def check_cell():
    while True:
        try:
            print("Enter coords: ")
            global coords_x, coords_y
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

def print_board_state():
    print('---------')
    print('|', og_board_state_parser[0], og_board_state_parser[1], og_board_state_parser[2], '|')
    print('|', og_board_state_parser[3], og_board_state_parser[4], og_board_state_parser[5], '|')
    print('|', og_board_state_parser[6], og_board_state_parser[7], og_board_state_parser[8], '|')
    print('---------')

def if_empty_replace(n):
    global og_board_state_parser
    if og_board_state_parser[n] == ('_' or ' '):
        og_board_state_parser[n] = 'X'
        # print(og_board_state_parser[n])
    else:
        print('This cell is occupied! Choose another one!')
        check_cell()

# convert board string X's and O's to list with each element as X or O
def get_board_state(field_input):
    global og_board_state_parser, og_board_state
    # print("Enter cells: ")
    og_board_state = field_input    #NOTE change to og_board_state() see above
    #Full string as individual string characters
    # og_board_state_parser = []
    for char in og_board_state:
        og_board_state_parser.append(char)


    # #Rows, columns, and diagnonals outcomes as a list with each element as a three letter string i.e. 'XXX' or 'XOO'
    # outcomes = [
    #     og_board_state[0:3],     #row 1
    #     og_board_state[3:6],     #row 2
    #     og_board_state[6:9],     #row 3
    #     og_board_state[0::3],    #column 1
    #     og_board_state[1::3],    #column 2
    #     og_board_state[2::3],    #column 3
    #     og_board_state[::4],     #diagonal 1
    #     og_board_state[2:7:2]    #diagonal 2
    # ]


og_board_state_parser = []

board_input = input("Enter cells:")
get_board_state(board_input)
print_board_state()
check_cell()
print_board_state()

# console print tests for vars
# print(og_board_state_parser)
# print(len(og_board_state_parser))
# print_board_state()
# print(coords_x)


# Flow control for main loop
    # if len(og_board_state) > 9:
    #     print("Too many characters for a 3 X 3 board. Try again.")
    # elif len(og_board_state_parser) < 9:
    #     print("Need more information to fill a 3 X 3 board. Try again.")
    # else:
    #     return og_board_state_parser