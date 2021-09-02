from graphics import *
import time
import random
import math
import gc
import sys

def intro_splash_screen():
    print("\n"*5)
    intro_splash = open("intro_graphics.txt", "r", encoding="utf-8")
    intro_splash_readlines = intro_splash.readlines()
    for line in intro_splash_readlines:
        print(line.strip("\n"))
        time.sleep(0.01)
    print("\r", end="")
    time.sleep(0.5)
    i=0
    while i < 104:
        print("\r" + "^"*i, end="")
        i+=1
        time.sleep(0.01)

    print()
    print("Welcome to #PLK PETRI DISH GAME 2020 1.0")

    user_input_splash ="empty"
    while user_input_splash != "Start" or user_input_splash != "start":
        user_input_splash = input("Type: \"Start\" to start the game "+
                                  "or \"Help\" for instructions. \n")
        if user_input_splash == "Start" or user_input_splash == "start":
            print()
            return

        elif user_input_splash == "Help" or user_input_splash == "help":
            print()
            print("******* HELP *******")
            print("Welcome to #PLK Petri Dish Game 2020 1.0")
            print()
            print("This is a game for three players. The main goal of the\n"+
                  "game is to create a better virus than the two other\n"+
                  "players have created. \n\n"+
                  "Each player is asked to enter their player name and\n"+
                  "their custom DNA sequence for their virus. The DNA\n"+
                  "sequence requires eight characters and can include only\n"+
                  "characters a, t, c, and g. Each character may be used \n"+
                  "as many times as wanted and not all of the characters\n"+
                  "are required to be used. DNA sequence can be for example\n"+
                  "any of the following: \"aattccgg\", \"aaatttgg\", or\n"+
                  "ccccccct. The four bases: ATCG, Adenine, thymine, cytosine\n"
                  "and guanine are the four nucleotides found in DNA.")
            print()
            print("Each of the characters (building blocks) in the DNA\n"+
                  "sequence represents different attributes of the virus.\n"+
                  "Different combinations of the attributes cause the \n"+
                  "virus to behave in different ways. The behavioral \n"+
                  "attributes that the virus may vary in include: \n"+
                  "growth speed, aggression, area, and spread in relation \n"+
                  "to the centre of the petri dish.")
            print()
            print("The virus growth terminates as it breaches the limits\n"+
                  "/ outer boundaries of the petri dish. The virus that \n"+
                  "acquired most area is the winning virus. Each player \n"+
                  "gets three petri dishes i.e. instances of their custom\n"+
                  "virus. The total area for each player is summed over \n"+
                  "these three virus instances.")

            print()

intro_splash_screen()

"""
players_entered = False

player_1 = input("Give name of player 1: ")
player_2 = input("Give name of player 2: ")
player_3 = input("Give name of player 3: ")
"""
time.sleep(1)
counter_start = time.time()
time.sleep(1)

"""
def clear(win):
    for item in win.items[1500:-1500]:
        item.undraw()
    gc.collect()
    win.update()
"""

def clear_all(win):
    i = 0
    for i in range(0, 200):
        for item in win.items:
            item.undraw()
            win.update()
            time.sleep(0.00001)
        i += 1
        string = ("Clearing element win." + "." * (i//4))
        sys.stdout.write("\r" + string)
        if i % 2 == 0:
            time.sleep(0.01)

    print()
    win.flush()
    win.update()
    gc.collect()

def sequence_generator(sequence_length, sequence_letters):
    string = ""
    while len(string) < 8:
        string = string + sequence_letters[random.randint(0,3)]
    return(string)

sequence_length = 8
sequence_letters = "atcg"

def sequence_letter_checker_ok(sequence):
    for letter in sequence:
        if letter not in sequence_letters:
            print("Incorrect sequence entered.")
            return False
        else:
            return True

player_names = []
player_sequences = []
for i in range(1, 4):
    player_sequence = ""
    player_input_string = "Enter player " + str(i) + " name (Max 8 characters). \n"
    player_name = input(player_input_string)
    print()
    while len(player_sequence) != 8 or sequence_letter_checker_ok(player_sequence) == False:
        player_sequence = input("Enter an 8 characters long string to form a DNA sequence.\n"
                                "The string can only include letters a, t, c, and g and \nmust be "
                                "8 characters long.\n")

    player_names.append(player_name)
    player_sequences.append(player_sequence)
    print()

win = GraphWin("Petrimalja", 1600, 1000, autoflush=False)

def main():

    player_1 = player_names[0]
    player_1_sequence = player_sequences[0]
    #player_1_sequence = sequence_generator(sequence_length, sequence_letters)

    player_2 = player_names[1]
    player_2_sequence = player_sequences[1]
    #player_2_sequence = sequence_generator(sequence_length, sequence_letters)

    player_3 = player_names[2]
    player_3_sequence = player_sequences[2]
    #player_3_sequence = sequence_generator(sequence_length, sequence_letters)

    fastest = "None"
    largest_area = "None"
    most_efficient = "None"


    print(player_1, player_1_sequence)
    print(player_2, player_2_sequence)
    print(player_3, player_3_sequence)


    players_entered = True
    clear_all(win)

    counter_start = time.time()
    time_now = time.time() - counter_start
    print(time_now)

    time_now_minutes = time_now // 60
    time_now_seconds = time_now % 60

    marker_zero_x, marker_zero_y = 602, 498
    marker_pxsec_zero_x, marker_pxsec_zero_y = 601, 851
    marker_likeliness_counter = 0

    if players_entered == True:
        #win = GraphWin("Petrimalja", 1600, 1000, autoflush=False)

        win.setBackground("black")

        x = 150
        y = 150
        coordinates_list = []
        for i in range(1, 4):
            for d in range(1, 4):
                coordinates_list.append([i*x, d*y])

        coordinates_original = []
        coordinates_timer_flag = []
        coordinates_area_counter = []

        for i in range(1, 4):
            for d in range(1, 4):
                coordinates_original.append([i*x, d*y])

        for i in range(1, 4):
            for d in range(1, 4):
                coordinates_area_counter.append([i*x, d*y])

        for item in coordinates_list:
            pt = Point(item[0], item[1])
            pt.setOutline("white")
            pt.draw(win)



        for item in coordinates_list:
            circle = Circle(Point(item[0], item[1]), 45)
            circle.setOutline("white")
            circle.draw(win)


        for item in coordinates_list:
            coordinates_timer_flag.append(0)

        i = 0
        ST = 20
        update_rate = 20

        X_SCALER = 0.08

        time_now = time.time() - counter_start
        overall_timer = str(
            "{:0<2}:{:05.2f}".format(int(time_now_minutes), time_now_seconds))
        overall_timer_print = Text(Point(100, 50), overall_timer)
        overall_timer_print.setFill("white")
        overall_timer_print.draw(win)

        chart_rectangle = Rectangle (Point(600, 100), Point(1400, 500))
        chart_rectangle.setOutline("white")
        chart_rectangle.draw(win)

        timer_vert_line = Line(Point(marker_zero_x, 100),
                               Point(marker_zero_x, 540))
        timer_vert_line.setFill("Grey")
        timer_vert_line.draw(win)

        timer_vert_line2 = Line(Point(marker_zero_x, 550),
                                Point(marker_zero_x, 850))
        timer_vert_line2.setFill("Grey")
        timer_vert_line2.draw(win)

        for i in range(600, 1400, 50):
            vertical_line = Line(Point(i, 100), Point(i, 500))
            vertical_line.setFill("Grey")
            vertical_line.draw(win)
            update(update_rate)

        for i in range(100, 500, 50):
            horizontal_line = Line(Point(600, i), Point(1400, i))
            horizontal_line.setFill("Grey")
            horizontal_line.draw(win)
            update(update_rate)


        area = 5920
        for i in range(100, 501, 50):
            area_marker = Text(Point(565, i), ("Area: {:<4}".format(area)))
            area_marker.setFill("White")
            area_marker.setSize(8)
            area_marker.draw(win)
            area -= 740
            update(update_rate)

        chart_rectangle = Rectangle (Point(600, 550), Point(1400, 850))
        chart_rectangle.setOutline("white")
        chart_rectangle.draw(win)

        for i in range(600, 1400, 50):
            vertical_line = Line(Point(i, 550), Point(i, 850))
            vertical_line.setFill("Grey")
            vertical_line.draw(win)
            update(update_rate)

        for i in range(550, 850, 50):
            horizontal_line = Line(Point(600, i), Point(1400, i))
            horizontal_line.setFill("Grey")
            horizontal_line.draw(win)
            update(update_rate)

        pxsec_text = Text(Point(565, 800), "13 px/s")
        pxsec_text.setFill("White")
        pxsec_text.setSize(8)
        pxsec_text.draw(win)

        pxsec_text = Text(Point(565, 750), "25 px/s")
        pxsec_text.setFill("White")
        pxsec_text.setSize(8)
        pxsec_text.draw(win)

        pxsec_text = Text(Point(565, 700), "38 px/s")
        pxsec_text.setFill("White")
        pxsec_text.setSize(8)
        pxsec_text.draw(win)

        pxsec_text = Text(Point(565, 650), "50 px/s")
        pxsec_text.setFill("White")
        pxsec_text.setSize(8)
        pxsec_text.draw(win)

        pxsec_text = Text(Point(565, 600), "63 px/s")
        pxsec_text.setFill("White")
        pxsec_text.setSize(8)
        pxsec_text.draw(win)

        player_1_circle = Circle(Point(120,550), 6)
        player_1_circle.setFill(color_rgb(255, 0, 255))
        player_1_circle.draw(win)

        player_2_circle = Circle(Point(270, 550), 6)
        player_2_circle.setFill(color_rgb(255, 255, 0))
        player_2_circle.draw(win)

        player_3_circle = Circle(Point(420, 550), 6)
        player_3_circle.setFill(color_rgb(0, 255, 255))
        player_3_circle.draw(win)

        column_a_area_printer = Text(Point(160, 550), player_1)
        column_a_area_printer.setFill("White")
        column_a_area_printer.draw(win)

        column_b_area_printer = Text(Point(310, 550), player_2)
        column_b_area_printer.setFill("White")
        column_b_area_printer.draw(win)

        column_c_area_printer = Text(Point(460, 550), player_3)
        column_c_area_printer.setFill("White")
        column_c_area_printer.draw(win)

        marker_likeliness_counter += 1


        initializing_text = Text(Point(250, 650), "Initializing...")
        initializing_text.setFill("White")
        initializing_text.setSize(36)
        initializing_text.draw(win)
        update()
        time.sleep(3)
        initializing_text.undraw()
        update()

        initializing_text = Text(Point(250, 650), "Starting round")
        initializing_text.setFill("White")
        initializing_text.setSize(36)
        initializing_text.draw(win)
        update()
        time.sleep(3)
        initializing_text.undraw()
        update()
        time.sleep(1)

        game_on = True

        while game_on == True:

            if coordinates_timer_flag.count(0) > 0:
                overall_timer_print.undraw()
                timer_vert_line.undraw()
                timer_vert_line2.undraw()

                time_now = time.time() - counter_start
                time_now_minutes = time_now // 60
                time_now_seconds = time_now % 60
                overall_timer = str(
                    "{:02}:{:05.2f}".format(int(time_now_minutes), time_now_seconds))
                overall_timer_print = Text(Point(marker_zero_x, 530), overall_timer)
                overall_timer_print.setFill("white")
                overall_timer_print.draw(win)

                timer_vert_line = Line(Point(marker_zero_x+2, 100), Point(marker_zero_x+2, 520))
                timer_vert_line.setFill("Grey")
                timer_vert_line.draw(win)

                timer_vert_line2 = Line(Point(marker_zero_x+2, 540), Point(marker_zero_x+2, 850))
                timer_vert_line2.setFill("Grey")
                timer_vert_line2.draw(win)

                column_a = (len(coordinates_area_counter[0]) - 1 +
                            len(coordinates_area_counter[1]) - 1 +
                            len(coordinates_area_counter[2]) - 1)

                column_b = (len(coordinates_area_counter[3]) - 1 +
                            len(coordinates_area_counter[4]) - 1 +
                            len(coordinates_area_counter[5]) - 1)

                column_c = (len(coordinates_area_counter[6]) - 1 +
                            len(coordinates_area_counter[7]) - 1 +
                            len(coordinates_area_counter[8]) - 1)

                column_a_scaled = column_a * 0.064
                column_b_scaled = column_b * 0.064
                column_c_scaled = column_c * 0.064

                likeliness = 9

                marker_zero_x += X_SCALER
                column_a_marker = Point((marker_zero_x), marker_zero_y - column_a_scaled)
                column_a_marker.setOutline(color_rgb(255, 0, 255))
                if marker_likeliness_counter % likeliness == 0:
                    column_a_marker.draw(win)

                marker_zero_x += X_SCALER
                column_a_marker = Point((marker_zero_x), marker_zero_y-1 - column_b_scaled)
                column_a_marker.setOutline(color_rgb(225, 255, 0))
                if marker_likeliness_counter % likeliness == 0:
                    column_a_marker.draw(win)

                marker_zero_x += X_SCALER
                column_a_marker = Point((marker_zero_x), marker_zero_y-2 - column_c_scaled)
                column_a_marker.setOutline(color_rgb(0, 255, 255))
                if marker_likeliness_counter % likeliness == 0:
                    column_a_marker.draw(win)

                time_now = time_now + 0.1

                marker_pxsec_zero_x += X_SCALER
                column_a_pxsec_marker = Point(marker_pxsec_zero_x,
                                              (marker_pxsec_zero_y -
                                               column_a / time_now)*4-2550)
                column_a_pxsec_marker.setFill(color_rgb(255, 0, 255))
                if marker_likeliness_counter % likeliness == 0 and (marker_pxsec_zero_y - column_a / time_now)*4-2550 > 550:
                    column_a_pxsec_marker.draw(win)

                marker_pxsec_zero_x += X_SCALER
                column_b_pxsec_marker = Point(marker_pxsec_zero_x,
                                              (marker_pxsec_zero_y -
                                               column_b / time_now)*4-2550)
                column_b_pxsec_marker.setFill(color_rgb(255, 255, 0))
                if marker_likeliness_counter % likeliness == 0 and (marker_pxsec_zero_y - column_b / time_now)*4-2550 > 550:
                    column_b_pxsec_marker.draw(win)

                marker_pxsec_zero_x += X_SCALER
                column_b_pxsec_marker = Point(marker_pxsec_zero_x,
                                              (marker_pxsec_zero_y -
                                               column_c / time_now)*4-2550)
                column_b_pxsec_marker.setFill(color_rgb(0, 255, 255))
                if marker_likeliness_counter % likeliness == 0 and (marker_pxsec_zero_y - column_c / time_now)*4-2550 > 550:
                    column_b_pxsec_marker.draw(win)

                marker_likeliness_counter += 1


            column_a_area_printer = Text(Point(160, 575), ("Area: {:>6}".format(column_a)))
            column_a_area_printer.setFill("White")
            column_a_area_printer.draw(win)

            column_b_area_printer = Text(Point(310, 575), ("Area: {:>6}".format(column_b)))
            column_b_area_printer.setFill("White")
            column_b_area_printer.draw(win)

            column_c_area_printer = Text(Point(460, 575), ("Area: {:>6}".format(column_c)))
            column_c_area_printer.setFill("White")
            column_c_area_printer.draw(win)

            column_a_pxsec_printer = Text(Point(160, 600), (
                "Px/Sec: {:05.2f}".format(column_a / time_now)))
            column_a_pxsec_printer.setFill("White")
            column_a_pxsec_printer.draw(win)

            column_b_pxsec_printer = Text(Point(310, 600), (
                "Px/Sec: {:05.2f}".format(column_b / time_now)))
            column_b_pxsec_printer.setFill("White")
            column_b_pxsec_printer.draw(win)

            column_c_pxsec_printer = Text(Point(460, 600), (
                "Px/Sec: {:05.2f}".format(column_c / time_now)))
            column_c_pxsec_printer.setFill("White")
            column_c_pxsec_printer.draw(win)


            for index, item in enumerate(coordinates_list, 0):

                ST = random.randint(1, random.randint(1, random.randint(1, random.randint(1, random.randint(1, random.randint(1, 25))))))

                if index <= 2:
                    sequence = player_1_sequence
                if index >= 3 <= 5:
                    sequence = player_2_sequence
                if index >= 6:
                    sequence = player_3_sequence

                time_now = time.time() - counter_start
                if time_now < random.randint(15, 35):
                    for i in range(0, sequence.count("a")):
                        ST += random.randint(0, random.randint(1, 13))
                        item[0] = coordinates_original[index][0] + random.randint(1, 2)
                        item[1] = coordinates_original[index][1] + random.randint(1, 2)

                for i in range(0, sequence.count("a")):
                    ST += random.randint(0, random.randint(0, random.randint(1, 3)))

                for i in range(0, sequence.count("c")):
                    if random.randint(1,700) == 1:
                        item[0] = coordinates_original[index][0] + random.randint(1, 9)
                        item[1] = coordinates_original[index][1] + random.randint(1, 9)

                time_now = time.time() - counter_start
                if time_now > (random.randint(15,25)) and time_now < 90:
                    for i in range(0, sequence.count("g")):
                        ST += random.randint(0, random.randint(1, 9))
                        item[0] = coordinates_original[index][0] + random.randint(1, 2)
                        item[1] = coordinates_original[index][1] + random.randint(1, 2)


                    time_now = time.time() - counter_start

                st = ST
                st = ST

                if time_now > 60:
                    st = st + random.randint(2, random.randint(2, random.randint(2, 8)))

                if time_now > (random.randint(180, 230)):
                    st = st + random.randint(2, random.randint(2, 8))

                if time_now > 300:
                    st = st + random.randint(3, random.randint(4, 16))

                if coordinates_timer_flag[index] != 1:
                    item[0] += (random.randint(-st, +st))
                    item[1] += (random.randint(-st, +st))

                    if [item[0], item[1]] not in coordinates_area_counter[index]:
                        coordinates_area_counter[index].append([item[0], item[1]])

                    for i in range(0, sequence.count("a")):
                        if random.randint(1, 60) == 1:
                            coordinates_area_counter[index].append([item[0]+random.randint(0,1), item[1]+random.randint(0,1)])


                    pt = Point(item[0], item[1])
                    pt.setOutline(color_rgb(random.randint(100, 150),
                                            random.randint(100, 254),
                                            random.randint(100, 150)))

                    if marker_likeliness_counter % likeliness == 0:
                        pt.draw(win)

                    distance = math.sqrt(abs(coordinates_original[index][0] -
                                             abs(item[0])) ** 2 +
                                         abs(coordinates_original[index][1] -
                                             abs(item[1])) ** 2)

                if distance >= 45 and coordinates_timer_flag[index] != 1:
                    circle = Circle(Point(coordinates_original[index][0],
                                          coordinates_original[index][1]), 45)
                    circle.setOutline("red")
                    circle.setWidth(2)
                    circle.draw(win)

                    time_now = time.time() - counter_start

                    time_now_minutes = time_now // 60
                    time_now_seconds = time_now % 60

                    time_print = str("{:02}:{:05.2f}".format(int(time_now_minutes),
                                                             time_now_seconds))
                    time_printer = Text(Point(coordinates_original[index][0],
                                              coordinates_original[index][1] + 60),
                                        time_print)
                    time_printer.setFill("white")
                    time_printer.draw(win)

                    coordinates_timer_flag[index] = 1
                    if fastest == "None":
                        if index <= 2:
                            fastest = "Player 1"
                        if index >= 3 <= 5:
                            fastest = "Player 2"
                        if index >= 6:
                            fastest = "Player 3"

                        fastest_time = str(time_now)[:6]

            update(25)
            column_a_area_printer.undraw()
            column_b_area_printer.undraw()
            column_c_area_printer.undraw()

            column_a_pxsec_printer.undraw()
            column_b_pxsec_printer.undraw()
            column_c_pxsec_printer.undraw()

            if 0 not in coordinates_timer_flag:
                game_on = False

    column_a_area_printer.draw(win)
    column_b_area_printer.draw(win)
    column_c_area_printer.draw(win)

    column_a_pxsec_printer.draw(win)
    column_b_pxsec_printer.draw(win)
    column_c_pxsec_printer.draw(win)

    len_a = len(coordinates_area_counter[0]) + len(coordinates_area_counter[1]) + len(coordinates_area_counter[2])
    len_b = len(coordinates_area_counter[3]) + len(coordinates_area_counter[4]) + len(coordinates_area_counter[5])
    len_c = len(coordinates_area_counter[6]) + len(coordinates_area_counter[7]) + len(coordinates_area_counter[8])

    areas = [len_a, len_b, len_c]
    largest_area = sorted(areas)[-1]

    if (len_a >= len_b) and (len_a >= len_c):
        largest = "Player 1"
    elif (len_b >= len_a) and (len_b >= len_c):
        largest = "Player 2"
    else:
        largest = "Player 3"

    game_over = Text(Point(300, 650), "Round Over")
    game_over.setSize(35)
    game_over.setFill("White")
    game_over.draw(win)

    game_over = Text(Point(300, 700), ("Fastest: " + fastest))
    game_over.setSize(18)
    game_over.setFill("White")
    game_over.draw(win)

    game_over = Text(Point(300, 735), ("Largest area: " + str(largest)))
    game_over.setSize(18)
    game_over.setFill("White")
    game_over.draw(win)

    update()

    if fastest == "Player 1":
        fastest_sequence = player_1_sequence
    if fastest == "Player 2":
        fastest_sequence = player_2_sequence
    if fastest == "Player 3":
        fastest_sequence = player_3_sequence

    if largest == "Player 1":
        largest_sequence = player_1_sequence
    if largest == "Player 2":
        largest_sequence = player_2_sequence
    if largest == "Player 3":
        largest_sequence = player_3_sequence

    global report_print
    report_print = {
        "largest_player" : largest,
        "largest_sequence" : largest_sequence,
        "largest_area" : largest_area,
        "fastest_player" : fastest,
        "fastest_sequence" : fastest_sequence,
        "fastest_time" : fastest_time
    }

    time.sleep(3)


main_counter = 0

file_object = open("execution_times-2020-10-12.txt", "a+")
header = "largest_player;largest_sequence;largest_area; " \
         "fastest_player;fastest_sequence;fastest_time;round_length \n"

file_object.write(header)

file_object.close()

for main_counter in range(0, 500):

    counter_start = time.time()

    global report_print
    report_print = {}

    main()
    main_counter += 1

    time_now = time.time() - counter_start
    time_now_minutes = time_now // 60
    time_now_seconds = time_now % 60

    file_object = open("execution_times-2020-10-12.txt", "a+")

    report_print["round_length"] = (str("{:02}:{:05.2f}".format(int(time_now_minutes),
                                                             time_now_seconds)))
    print_string = ""
    for key, value in report_print.items():
        print_string += (str(value) + ";")
    print()
    print("----------------")
    for key, value in report_print.items():
        print(key, value)
    print("----------------")
    print()

    file_object.write(print_string + "\n")
    file_object.close()

