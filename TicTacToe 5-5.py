# check cells to see if they are empty or not and replace with X or O if empty
def check_cell():
    while True:
        try:
            global coords_x, coords_y
            coords_x, coords_y = input("Enter coords:").split(" ")
            coords_x = int(coords_x)
            coords_y = int(coords_y)
            if coords_x < 1 or coords_x > 3 or coords_y < 1 or coords_y >3:
                print("Coordinates should be from 1 to 3!")
                check_cell()
            elif coords_x == 1:
                if coords_y == 1:
                    print(og_board_state_parser[6])
                    replace(6)
                elif coords_y == 2:
                    print(og_board_state_parser[3])
                    replace(3)
                elif coords_y == 3:
                    print(og_board_state_parser[0])
                    replace(0)
            elif coords_x == 2:
                if coords_y == 1:
                    print(og_board_state_parser[7])
                    replace(7)
                elif coords_y == 2:
                    print(og_board_state_parser[4])
                    replace(4)
                elif coords_y == 3:
                    print(og_board_state_parser[1])
                    replace(1)
            elif coords_x == 3:
                if coords_y == 1:
                    print(og_board_state_parser[8])
                    replace(8)
                elif coords_y == 2:
                    print(og_board_state_parser[5])
                    replace(5)
                elif coords_y == 3:
                    print(og_board_state_parser[2])
                    replace(2)
            else:
                print("Problem, try again.")
                check_cell()
            break
        except ValueError:
            print("You should enter numbers")
            check_cell()
            break


# determins if cell on gameboard is empty and replace with X respectively
def replace(n):
    global og_board_state_parser
    if og_board_state_parser[n] == "_" or og_board_state[n] == " ":
        if x_turn == True:
            og_board_state_parser[n] = "X"
        elif x_turn == False:
            og_board_state_parser[n] = "O"
        # print(og_board_state_parser[n])
    else:
        print('This cell is occupied! Choose another one!')
        check_cell()


# prints game board status onto console
def print_board_state():
    print('---------')
    print('|', og_board_state_parser[0], og_board_state_parser[1], og_board_state_parser[2], '|')
    print('|', og_board_state_parser[3], og_board_state_parser[4], og_board_state_parser[5], '|')
    print('|', og_board_state_parser[6], og_board_state_parser[7], og_board_state_parser[8], '|')
    print('---------')



# convert board string X's and O's to list with each element as X or O
def parse_board_state(field_input):
    global og_board_state_parser, og_board_state
    # print("Enter cells: ")
    og_board_state = field_input    #NOTE change to og_board_state() see above
    for char in og_board_state:
        og_board_state_parser.append(char)


def check_winning():    #Rows, columns, and diagnonals outcomes as a list with each element as a three letter string i.e. 'XXX' or 'XOO'

    global winning, someone

    outcomes = [
        og_board_state_parser[3:6],     #row 2
        og_board_state_parser[0:3],     #row 1
        og_board_state_parser[6:9],     #row 3
        og_board_state_parser[0::3],    #column 1
        og_board_state_parser[1::3],    #column 2
        og_board_state_parser[2::3],    #column 3
        og_board_state_parser[::4],     #diagonal 1
        og_board_state_parser[2:7:2]    #diagonal 2
    ]

    # determines if x wins
    for i in range(len(outcomes)):
        if outcomes[i] == ["X", "X", "X"]:
            someone = "X"
            print('X wins')
            winning = True
            break
        elif outcomes[i] == ["O", "O", "O"]:
            someone = "O"
            print("O wins")
            winning = True
            break
        else:
            pass

def check_empty():

    global empty_present

    for x in og_board_state_parser:
        for i in x:
            if i == "_" or x == " ":
                empty_present = True
                break
            else:
                empty_present = False

# initialize variables
og_board_state_parser = []
empty_present = True
x_turn = True
winning = False
someone = "no one"

# initialize empty board state
parse_board_state("123456789")
print_board_state()
print(og_board_state_parser)

# game loop
while True:
    check_winning()
    check_empty()
    print(f"empty_present: {empty_present}")
    print(f"winning: {winning}")
    print(f"someone: {someone}")
    if winning == True:
        print_board_state()
        print(f"{someone} wins!")
        break
    elif empty_present == False and winning == False:
        print("Draw")
        # parse_board_state("         ")
        break
    elif empty_present == True:
        print("Empty present")
    check_cell()
    print_board_state()
    if x_turn == True:
        x_turn = False
    elif x_turn == False:
        x_turn = True
