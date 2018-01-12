# this will be the main GUI
# v11 - Final - v.1.0

import tkinter
from tkinter import *
from random import *

# global vars
allPlayers = [1, 2]
current_player = None
player_data = ["Player 1", "Player 2"]     # will be changed so that the settings will change these defaults
moves = 0
winMes = None
doubleMes = None
startMes = None
preload = False

p1_loc = 0
p2_loc = 0

obs1_info = None
obs2_info = None
obs3_info = None
obs4_info = None

board = [3, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0]
# this is now a normal 1d array/list

# values in the board mean certain things:
# 1 means player1 is in the slot
# 2 means player2 is in the slot
# 3 means both player1 and player2 are in the slot
# 4 means there is an obstacle in the slot
# will add more values in the future


def read_in_messages():
    # imports the global message vars
    global winMes
    global doubleMes
    global startMes

    # opens the files and dumps the contents of them into the appropriate global variable
    # win message
    file = open("win.txt", "r")
    winMes = file.read()
    file.close()

    # double message
    file = open("double.txt", "r")
    doubleMes = file.read()
    file.close()

    # start message
    file = open("start.txt", "r")
    startMes = file.read()
    file.close()

    # for testing
    # print(winMes + "\n" + doubleMes + "\n" + startMes)


def victory_event():
    global current_player

    # turns off the button so the game cannot be continued after game is over
    btnRoll.configure(state=DISABLED)

    print("EVENT - Victory for " + get_player_name(current_player))

    # from here on is the tkinter code for the GUI
    victory_root = tkinter.Tk()

    # this new function that I added fixes the problem where the exit button would only close the main window
    # it first destroys the victory window and the call the function that destroys the main window
    def leave():
        victory_root.destroy()
        exit_game()

    victory_root.iconbitmap('icon.ico')

    lbl_message = tkinter.Label(victory_root, text=winMes).pack()

    btn_vic_exit = tkinter.Button(victory_root, text="Exit Game", command=leave).pack()

    victory_root.mainloop()


def start_event():
    victory_root = tkinter.Tk()

    print("EVENT - Game Start")

    def leave():
        victory_root.destroy()

    victory_root.iconbitmap('icon.ico')
    lbl_message = tkinter.Label(victory_root, text=startMes).pack()
    btn_vic_exit = tkinter.Button(victory_root, text="Close", command=leave).pack()

    # there is no root.mainloop() as it breaks the program


def double_event():
    global current_player

    print("EVENT - Double Rolled by " + get_player_name(current_player))

    # the names of the roots are from the original function this was based on: victory_event()
    victory_root = tkinter.Tk()

    def leave():
        victory_root.destroy()

    victory_root.iconbitmap('icon.ico')
    lbl_message = tkinter.Label(victory_root, text=doubleMes).pack()
    btn_vic_exit = tkinter.Button(victory_root, text="Close", command=leave).pack()

    # there is no root.mainloop() as it breaks the program


def get_player_name(player):
    global player_data
    # the -1 is as you give the player number so if you want player 2 you give 2 and 2 is an out of index
    # player 2 is equal to the second element of player_data or number 1 element
    return player_data[player-1]


def help_box():
    help_root = tkinter.Tk()

    def exit_help():
        help_root.destroy()

    help_root.iconbitmap('icon.ico')

    # labels detailing how to play the game, an instruction guide
    lbl_info1 = tkinter.Label(help_root, text="Welcome to the Official Dice Game™. Disregard all others, as "
                                              "they are inferior.").pack()
    lbl_info2 = tkinter.Label(help_root, text="In this game, you both have to compete against each other in a "
                                              "game of rolling dice and moving tokens around a board.").pack()
    lbl_info3 = tkinter.Label(help_root, text="The main object of the Official Dice Game™ is to reach the last "
                                              "square on the board to the left of the screen before other player/s do."
                                              " On the way there you will encounter trials, tribulations,"
                                              " and other words that begin with ‘t’.").pack()
    lbl_info4 = tkinter.Label(help_root, text="Pressing the roll button on your turn will send your player forwards "
                                              "the number of spaces on the dice that were just rolled. Neato. But be "
                                              "wary! If you roll the same number on both dice, you get sent backwards"
                                              " that number of spaces instead.").pack()
    lbl_info5 = tkinter.Label(help_root, text="After you have rolled and your character has moved, then the game "
                                              "automatically switches the turns to the next player, and so on until "
                                              "someone wins. Studies show that all games of the Official Dice Game™"
                                              " take at minimum 5 seconds and at maximum 1 day to complete.").pack()
    lbl_info6 = tkinter.Label(help_root, text="On the board are various squares which will either send you forwards or"
                                              " knock you backwards. They can turn a losing turn into a "
                                              "winning one.").pack()
    lbl_info7 = tkinter.Label(help_root, text="Congratulation, you can now play the Official Dice Game™.").pack()

    btn_exit = tkinter.Button(help_root, text="Close", command=exit_help).pack()
        
    help_root.mainloop()


def change_btn_color():
    # if the player is 1 then the button will turn blue
    if current_player == 2:
        btnRoll.configure(bg="light sky blue")
    # otherwise it is player 2 and will change to light red
    elif current_player == 1:
        btnRoll.configure(bg="orange red")
    # the default colour of the button is grey


def exit_game():
    # this was my old solution but I replaced it with the exit() as it
    # closed all the window no matter how many the users has opened
    root.destroy()
    # exit()
    # note exit() does not work on school computers


root = tkinter.Tk()

# the grid as an image
image = tkinter.PhotoImage(file="grid.gif")
canvas = Canvas(width=image.width() + 5, height=image.height() + 5)
canvas.place(x=10, y=10)
canvas.create_image(image.width() / 2, image.height() / 2, image=image)


def render_obs():
    global obs1_info
    global obs2_info
    global obs3_info
    global obs4_info

    i = 0

    obs1_loc = int(obs1_info[0])

    while i != obs1_loc:
        if i <= 5:
            canvas.move(obs1, 109, 0)
        elif i == 6:
            canvas.move(obs1, 0, -91)
        elif 7 <= i <= 12:
            canvas.move(obs1, -109, 0)
        elif i == 13:
            canvas.move(obs1, 0, -94)
        elif 14 <= i <= 19:
            canvas.move(obs1, 109, 0)
        elif i == 20:
            canvas.move(obs1, 0, -96)
        elif 21 <= i <= 26:
            canvas.move(obs1, -109, 0)
        elif i == 27:
            canvas.move(obs1, 0, -94)
        elif 28 <= i <= 33:
            canvas.move(obs1, 109, 0)
        elif i == 34:
            canvas.move(obs1, 0, -94)
        elif 35 <= i <= 40:
            canvas.move(obs1, -109, 0)
        elif i == 41:
            canvas.move(obs1, 0, -94)
        elif 42 <= i < 48:
            canvas.move(obs1, 109, 0)

        i += 1

    i = 0

    obs2_loc = int(obs2_info[0])

    while i != obs2_loc:
        if i <= 5:
            canvas.move(obs2, 109, 0)
        elif i == 6:
            canvas.move(obs2, 0, -91)
        elif 7 <= i <= 12:
            canvas.move(obs2, -109, 0)
        elif i == 13:
            canvas.move(obs2, 0, -94)
        elif 14 <= i <= 19:
            canvas.move(obs2, 109, 0)
        elif i == 20:
            canvas.move(obs2, 0, -96)
        elif 21 <= i <= 26:
            canvas.move(obs2, -109, 0)
        elif i == 27:
            canvas.move(obs2, 0, -94)
        elif 28 <= i <= 33:
            canvas.move(obs2, 109, 0)
        elif i == 34:
            canvas.move(obs2, 0, -94)
        elif 35 <= i <= 40:
            canvas.move(obs2, -109, 0)
        elif i == 41:
            canvas.move(obs2, 0, -94)
        elif 42 <= i < 48:
            canvas.move(obs2, 109, 0)

        i += 1

    i = 0

    obs3_loc = int(obs3_info[0])

    while i != obs3_loc:
        if i <= 5:
            canvas.move(obs3, 109, 0)
        elif i == 6:
            canvas.move(obs3, 0, -91)
        elif 7 <= i <= 12:
            canvas.move(obs3, -109, 0)
        elif i == 13:
            canvas.move(obs3, 0, -94)
        elif 14 <= i <= 19:
            canvas.move(obs3, 109, 0)
        elif i == 20:
            canvas.move(obs3, 0, -96)
        elif 21 <= i <= 26:
            canvas.move(obs3, -109, 0)
        elif i == 27:
            canvas.move(obs3, 0, -94)
        elif 28 <= i <= 33:
            canvas.move(obs3, 109, 0)
        elif i == 34:
            canvas.move(obs3, 0, -94)
        elif 35 <= i <= 40:
            canvas.move(obs3, -109, 0)
        elif i == 41:
            canvas.move(obs3, 0, -94)
        elif 42 <= i < 48:
            canvas.move(obs3, 109, 0)

        i += 1

    i = 0

    obs4_loc = int(obs4_info[0])

    while i != obs4_loc:
        if i <= 5:
            canvas.move(obs4, 109, 0)
        elif i == 6:
            canvas.move(obs4, 0, -91)
        elif 7 <= i <= 12:
            canvas.move(obs4, -109, 0)
        elif i == 13:
            canvas.move(obs4, 0, -94)
        elif 14 <= i <= 19:
            canvas.move(obs4, 109, 0)
        elif i == 20:
            canvas.move(obs4, 0, -96)
        elif 21 <= i <= 26:
            canvas.move(obs4, -109, 0)
        elif i == 27:
            canvas.move(obs4, 0, -94)
        elif 28 <= i <= 33:
            canvas.move(obs4, 109, 0)
        elif i == 34:
            canvas.move(obs4, 0, -94)
        elif 35 <= i <= 40:
            canvas.move(obs4, -109, 0)
        elif i == 41:
            canvas.move(obs4, 0, -94)
        elif 42 <= i < 48:
            canvas.move(obs4, 109, 0)

        i += 1


def gen_obs():
    global obs1_info
    global obs2_info
    global obs3_info
    global obs4_info

    file = open("obs.txt", "r")
    import_txt = file.read()
    file.close()

    split_arr = import_txt.split(",")

    # info[0] = location
    # info[1] = + or -
    # info[2] = magnitude

    obs1_info = split_arr[0].split("_")
    obs2_info = split_arr[1].split("_")
    obs3_info = split_arr[2].split("_")
    obs4_info = split_arr[3].split("_")

    print(obs1_info)
    print(obs2_info)
    print(obs3_info)
    print(obs4_info)

    board[int(obs1_info[0])] = 4
    board[int(obs2_info[0])] = 4
    board[int(obs3_info[0])] = 4
    board[int(obs4_info[0])] = 4

    render_obs()


def obs_col(location):
    global obs1_info
    global obs2_info
    global obs3_info
    global obs4_info

    print("Obstacle at " + str(location) + " collided with.")

    if location == int(obs1_info[0]):
        val = int(obs1_info[2])

        if obs1_info[1] == "-":
            val -= (val * 2)

        obs_move(val, 1)

    elif location == int(obs2_info[0]):
        val = int(obs2_info[2])

        if obs2_info[1] == "-":
            val -= (val * 2)

        obs_move(val, 2)

    elif location == int(obs3_info[0]):
        val = int(obs3_info[2])

        if obs3_info[1] == "-":
            val -= (val * 2)

        print("val= " + str(val))
        obs_move(val, 3)

    elif location == int(obs4_info[0]):
        val = int(obs4_info[2])

        if obs4_info[1] == "-":
            val -= (val * 2)

        obs_move(val, 4)


def move_player_sprite(mag):
    global current_player
    global p1_loc
    global p2_loc

    if mag < 0:
        mag = mag * (-1)

        if current_player == 1:
            i = 0
            
            while i != mag:
                if p1_loc <= 6:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 7:
                    canvas.move(sprite_p1, 0, 91)
                elif 8 <= p1_loc <= 13:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 14:
                    canvas.move(sprite_p1, 0, 94)
                elif 15 <= p1_loc <= 20:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 21:
                    canvas.move(sprite_p1, 0, 96)
                elif 22 <= p1_loc <= 27:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 28:
                    canvas.move(sprite_p1, 0, 94)
                elif 29 <= p1_loc <= 34:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 35:
                    canvas.move(sprite_p1, 0, 94)
                elif 36 <= p1_loc <= 41:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 42:
                    canvas.move(sprite_p1, 0, 94)
                elif 43 <= p1_loc < 48:
                    canvas.move(sprite_p1, -109, 0)

                i += 1
                p1_loc -= 1

        elif current_player == 2:
            i = 0
            while i != mag:
                if p2_loc <= 6:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 7:
                    canvas.move(sprite_p2, 0, 91)
                elif 8 <= p2_loc <= 13:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 14:
                    canvas.move(sprite_p2, 0, 94)
                elif 15 <= p2_loc <= 20:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 21:
                    canvas.move(sprite_p2, 0, 96)
                elif 22 <= p2_loc <= 27:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 28:
                    canvas.move(sprite_p2, 0, 94)
                elif 29 <= p2_loc <= 34:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 35:
                    canvas.move(sprite_p2, 0, 94)
                elif 36 <= p2_loc <= 41:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 42:
                    canvas.move(sprite_p2, 0, 94)
                elif 43 <= p2_loc < 48:
                    canvas.move(sprite_p2, -109, 0)

                i += 1
                p2_loc -= 1
    else:
        if current_player == 1:
            i = 0

            while i != mag:
                if p1_loc <= 5:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 6:
                    canvas.move(sprite_p1, 0, -91)
                elif 7 <= p1_loc <= 12:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 13:
                    canvas.move(sprite_p1, 0, -94)
                elif 14 <= p1_loc <= 19:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 20:
                    canvas.move(sprite_p1, 0, -96)
                elif 21 <= p1_loc <= 26:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 27:
                    canvas.move(sprite_p1, 0, -94)
                elif 28 <= p1_loc <= 33:
                    canvas.move(sprite_p1, 109, 0)
                elif p1_loc == 34:
                    canvas.move(sprite_p1, 0, -94)
                elif 35 <= p1_loc <= 40:
                    canvas.move(sprite_p1, -109, 0)
                elif p1_loc == 41:
                    canvas.move(sprite_p1, 0, -94)
                elif 42 <= p1_loc < 48:
                    canvas.move(sprite_p1, 109, 0)

                i += 1
                p1_loc += 1

        elif current_player == 2:
            i = 0

            while i != mag:
                if p2_loc <= 5:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 6:
                    canvas.move(sprite_p2, 0, -91)
                elif 7 <= p2_loc <= 12:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 13:
                    canvas.move(sprite_p2, 0, -94)
                elif 14 <= p2_loc <= 19:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 20:
                    canvas.move(sprite_p2, 0, -96)
                elif 21 <= p2_loc <= 26:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 27:
                    canvas.move(sprite_p2, 0, -94)
                elif 28 <= p2_loc <= 33:
                    canvas.move(sprite_p2, 109, 0)
                elif p2_loc == 34:
                    canvas.move(sprite_p2, 0, -94)
                elif 35 <= p2_loc <= 40:
                    canvas.move(sprite_p2, -109, 0)
                elif p2_loc == 41:
                    canvas.move(sprite_p2, 0, -94)
                elif 42 <= p2_loc < 48:
                    canvas.move(sprite_p2, 109, 0)

                i += 1
                p2_loc += 1


def obs_move(distance, ob):
    global obs1_info
    global obs2_info
    global obs3_info
    global obs4_info

    if ob == 1:
        if distance < 0:  # if neg numb
            if int(obs1_info[0]) + distance < 0:
                set_location(0)
                print("move -- --0")
            else:
                set_location(int(obs1_info[0]) + distance)
                print("move -- ++"+str(distance))
        else:  # if pos numb
            set_location(int(obs1_info[0]) + distance)

    elif ob == 2:
        if distance < 0:  # if neg numb
            if int(obs2_info[0]) + distance < 0:
                set_location(0)
                print("move -- --0")
            else:
                set_location(int(obs2_info[0]) + distance)
                print("move -- ++"+str(distance))
        else:  # if pos numb
            set_location(int(obs2_info[0]) + distance)

    elif ob == 3:
        if distance < 0:  # if neg numb
            if int(obs3_info[0]) + distance < 0:
                set_location(0)
                print("move -- --0")
            else:
                set_location(int(obs3_info[0]) + distance)
                print("move -- ++"+str(distance))
        else:  # if pos numb
            set_location(int(obs3_info[0]) + distance)

    elif ob == 4:
        if distance < 0:  # if neg numb
            if int(obs4_info[0]) + distance < 0:
                set_location(0)
                print("move -- --0")
            else:
                set_location(int(obs4_info[0]) + distance)
                print("move -- ++"+str(distance))
        else:  # if pos numb
            set_location(int(obs4_info[0]) + distance)


    move_player_sprite(distance)


def print_board_console():
    #  for row in range(y):
    #     print(board[y-1])
    # this function prints the board to the console
    # 0 means nothing there
    # 1, 2, 3, etc is the player with their corresponding number
    # obstacles in the works

    # new code

    # this prints them in rows like before
    print(board[0:7])
    print(board[7:14])
    print(board[14:21])
    print(board[21:28])
    print(board[28:35])
    print(board[35:42])
    print(board[42:49])


def next_player():    # done works
    # this first check is to ensure that the first player is player1
    global current_player
    global moves
    print("next player func activated")
    if moves == 0:
        current_player = allPlayers[randint(0, 1)]
        change_btn_color()
    else:
        # iterations is an even number
        if current_player == 1:
            # sets next player to player2
            current_player = allPlayers[1]
            # iterations is an odd number
        elif current_player == 2:
            # sets next player to player1
            current_player = allPlayers[0]
        else:
            print("error in next_player func")
            # can use for future additions to the game like new players
    moves += 1
    change_btn_color()
    print(str(moves) + " moves")


def find_location():        # done may not work
    global current_player
    location = 0
    if current_player == 1:
        for i in range(len(board)):
            # only player1 in the slot
            if board[i] == 1:
                location = i
                print("find_location -- Located Player 1 at square " + str(i+1))
            # player1 and player2 in the slot
            elif board[i] == 3:
                location = i
                print("find_location -- Located Player 1 at square " + str(i+1))
    elif current_player == 2:
        for i in range(len(board)):
            # only player2 in the slot
            if board[i] == 2:
                location = i
                print("find_location -- Located Player 2 at square " + str(i+1))
            # player1 and player2 in the slot
            elif board[i] == 3:
                location = i
                print("find_location -- Located Player 2 at square " + str(i+1))

    return location


def set_location(new_location):     # done may not work
    global current_player
    # new_location -= 1
    # will set the current players location to the provided location on the board
    if current_player == 1:
        if board[48] == 1:
            victory_event()

        # the first part will get rid of any instances of the player already on the board
        for i in range(len(board)):
            # print("For loop number: " + str(i) + "-----Square: " + str(i + 1))
            # only player1 in the slot
            if board[i] == 1:
                board[i] = 0
                print("set_location -- Located 1 at square " + str(i+1))
            # player1 and player2 in the slot
            elif board[i] == 3:
                board[i] = 2
                print("set_location -- Located 3 at square " + str(i+1))
        # then this second part will set the new location to having an instance of the player

        # this sees if the new location has player2 already
        # if it does then it will set the location to a 3 meaning that both are in the same slot
        # if there is nothing in the slot then the slot is set to a 1 meaning that only player1 is located there
        try:
            if board[new_location] == 4:
                obs_col(new_location)
            elif board[new_location] == 2:
                board[new_location] = 3
            elif board[new_location] == 0:
                board[new_location] = 1
            else:
                print("Error in set_location for Player1")
        except IndexError:
            victory_event()

    elif current_player == 2:
        if board[48] == 2:
            victory_event()

        # the first part will get rid of any instances of the player already on the board
        for i in range(len(board)):
            # print("For loop number: " + str(i) + "-----Square: " + str(i + 1))
            # only player2 in the slot
            if board[i] == 2:
                board[i] = 0
                print("set_location -- Located 1 at square " + str(i+1))
            # player1 and player2 in the slot
            elif board[i] == 3:
                board[i] = 1
                print("set_location -- Located 3 at square " + str(i+1))
        # then this second part will set the new location to having an instance of the player

        # this sees if the new location has player1 already
        # if it does then it will set the location to a 3 meaning that both are in the same slot
        # if there is nothing in the slot then the slot is set to a 2 meaning that only player2 is located there
        try:
            if board[new_location] == 4:
                obs_col(new_location)
            elif board[new_location] == 1:
                board[new_location] = 3
            elif board[new_location] == 0:
                board[new_location] = 2
            else:
                print("Error in set_location for Player2")
        except IndexError:
            victory_event()


def dice_random():
    global moves
    dice_val1 = randint(1, 6)
    dice_val2 = randint(1, 6)

    # dice_val1 = 4
    # dice_val2 = 4
    #
    # if moves == 1:
    #     dice_val1 = 2
    #     dice_val2 = 4
    # elif moves == 3:
    #     dice_val1 = 4
    #     dice_val2 = 4

    return dice_val1, dice_val2


def player_move_value():
    d1, d2 = dice_random()
    print(d1, d2)
    result = d1 + d2
    if d1 == d2:
        double_event()
        print(result - (result * 2))
        return result - (result * 2)
    else:
        return result


def move(distance):
    # this func will move the player the amount of tiles and set the new location on the computer board
    location = find_location()
    print("MOVE -- Location:" + str(location))
    if distance < 0:  # if neg numb
        if location + distance < 0:
            set_location(0)
            print("MOVE -- Move value:" + str(location * -1))
            move_player_sprite(location * -1)
            print("move -- --0")
        else:
            set_location(location + distance)
            move_player_sprite(distance)
            print("move -- ++0")
    else:  # if pos numb
        set_location(location + distance)
        move_player_sprite(distance)


def roll():
    global current_player
    global moves
    global preload

    if preload == False:
        preload = True
        gen_obs()
        read_in_messages()
        start_event()
        btnRoll["text"] = "ROLL"
        next_player()
    else:
        print("roll")

        if moves == 0:
            move(player_move_value())
            print_board_console()

            print(get_player_name(current_player))
            print("-------------------------------------------")
        else:
            next_player()
            move(player_move_value())
            print_board_console()

            print(get_player_name(current_player))
            print("-------------------------------------------")


# main GUI code:

root.wm_attributes("-transparentcolor", "#ff00ff")
# root.configure(background='#ff00ff')

root.iconbitmap('icon.ico')
root.wm_title("Dice Game")
root.wm_minsize(1035, 685)

img1 = tkinter.PhotoImage(file="obs_sprite.gif")
obs1 = canvas.create_image(62, 614, image=img1)

img2 = tkinter.PhotoImage(file="obs_sprite.gif")
obs2 = canvas.create_image(62, 614, image=img2)

img3 = tkinter.PhotoImage(file="obs_sprite.gif")
obs3 = canvas.create_image(62, 614, image=img3)

img4 = tkinter.PhotoImage(file="obs_sprite.gif")
obs4 = canvas.create_image(62, 614, image=img4)

image_p1 = tkinter.PhotoImage(file="p1_sprite.gif")
sprite_p1 = canvas.create_image(33, 614, image=image_p1)

image_p2 = tkinter.PhotoImage(file="p2_sprite.gif")
sprite_p2 = canvas.create_image(89, 614, image=image_p2)

# some buttons
btnExit = tkinter.Button(root, text="EXIT", command=exit_game, bg="red", height=10, width=30)
btnHelp = tkinter.Button(root, text="HELP", command=help_box, height=10, width=30)
btnRoll = tkinter.Button(root, text="LOAD OBSTACLES", command=roll, height=10, width=30)

btnExit.place(relheight=0.333, x=1020, rely=0.2, anchor=E)
btnHelp.place(relheight=0.333, x=1020, rely=0.5, anchor=E)
btnRoll.place(relheight=0.333, x=1020, rely=0.8, anchor=E)

root.mainloop()
