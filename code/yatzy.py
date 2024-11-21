import yatzy_functions 
import random

def main():

    # Variables for avoiding "magic" numbers
    player_limit = { "min": 1, "max": 6 }
    maximum_rerolls = 2
    maximum_name_length = 8
    players_amount = 0
    dices_amount = 6
    players_amount = yatzy_functions.safe_int_input(player_limit["min"], player_limit["max"],  # Restrictions for amount of players
                                    f"How much players will play? (minimum is {player_limit["min"]}, maximum is {player_limit["max"]}): ")  # Message for user

    players = yatzy_functions.generate_players(players_amount)

    global_combination_number = 0
    all_combinations = {}
    for section in players["Player 1"]["combinations"]:
        for combination in players["Player 1"]["combinations"][section]:
            global_combination_number += 1
            all_combinations[global_combination_number] = { "section": section, "combination": combination }

    if players_amount == 1:
        print("Single player. Pick mode:\n1. Easy\n2. Medium\n3. Hard")
        mode = yatzy_functions.safe_int_input(1, 3, "\n==> ")
        minimum_points = [random.randint(50, 150), random.randint(150, 250), random.randint(250, 350)][mode]

    game_over = False
    while not game_over:
        for player in players:

            if not players[player]["available"]:
                continue
    


            print("═" * 100)
            yatzy_functions.render_box(f"{players[player]["name"]}, your turn!")
            print("═" * 100)
    
            rerolls = maximum_rerolls
            # dices = yatzy_functions.get_dices()   
            dices = [1, 2, 3, 4, 6, 1]

            players[player]["current dices"] = dices[:]  # Added [:] to create a new massive

            unused_combinations = {}
            available_combinations = {}
            available_combination_number = unused_combination_number = 0
            for section in players[player]["combinations"]:
                for combination in players[player]["combinations"][section]:
                    not_used = players[player]["combinations"][section][combination]["points"] == -1
                    available = players[player]["combinations"][section][combination]["function"](dices)
                    if not_used:
                        unused_combination_number += 1
                        unused_combinations[unused_combination_number] = { "section": section, "combination": combination }
                        if available:
                            available_combination_number += 1
                            available_combinations[available_combination_number] = { "section": section, "combination": combination }
    
            if len(available_combinations):    
                print("Your scoresheet:")
                print("┏" + "━" * 17 + "┳" + "━"*5 + "┓")

                combination_number = 1
                section = all_combinations[combination_number]["section"]
                combination = all_combinations[combination_number]["combination"]
                points = players[player]["combinations"][section][combination]["points"]
                if points == -1:
                        points = '-'
                while combination_number < len(all_combinations):
                    print("┃ {:<15} ┃ ".format(combination), end='')
                    print("{:<3} ┃".format(points))
                    print("┣" + "━" * 17 + "╋" + "━" * 5 + "┫")
                    combination_number += 1
                    section = all_combinations[combination_number]["section"]
                    combination = all_combinations[combination_number]["combination"]
                    points = players[player]["combinations"][section][combination]["points"]
                    if points == -1:
                        points = '-'
                print("┃ {:<15} ┃ ".format(combination), end='')
                print("{:<3} ┃".format(points))
                print("┗" + "━" * 17 + "┻" + "━" * 5 + "┛" + '\n')

                print("═" * 100)
                yatzy_functions.render_box(f"Your dices: {dices}") 
                print("═" * 100)
                print("\nAvailable combinations: ") 
                combination_number = 1
                while combination_number <= len(available_combinations):
                    section = available_combinations[combination_number]["section"]
                    print("━"*100 + f"\n{available_combinations[combination_number]["section"]}:\n")
                    while combination_number <= len(available_combinations) and section == available_combinations[combination_number]["section"]:
                        print(f"{combination_number}. { available_combinations[combination_number]["combination"] }")
                        combination_number += 1
                print("━"*100 + "\n")
                user_choice = yatzy_functions.safe_int_input(0, available_combination_number, "\nPick combination which you want to use or 0 if you want to cross\n○ ")
            else:
                print("═" * 100)
                yatzy_functions.render_box(f"Your dices: {dices}")
                print("═" * 100)
                user_choice = 0
                print("There is no available combinations for your dices :(\n")


            if not (len(available_combinations) and user_choice):
                print("Your unused combinations:\n")
                for combination_number in unused_combinations:
                    print(f"{combination_number}. {unused_combinations[combination_number]["combination"]}")
                user_choice = yatzy_functions.safe_int_input(1, unused_combination_number, "Pick which combination you want to cross\n✖ ")
                section = unused_combinations[user_choice]["section"]
                combination = unused_combinations[user_choice]["combination"]
                players[player]["combinations"][section][combination]["points"] = 0
            else:
                section = available_combinations[user_choice]["section"]
                combination = available_combinations[user_choice]["combination"]
                players[player]["combinations"][section][combination]["points"] = players[player]["combinations"][section][combination]["function"](dices)
    
            if len(unused_combinations) - 1 == 0:
                players[player]["available"] = False

            # print(f"Player: {players[player]}")
            

        game_over = set([players[f"Player {player_number}"]["available"] for player_number in range(1, players_amount + 1)]) == {0}


    print("\n" * 10)
    print("╤" * 100 + "\n")

    if players_amount == 1:
        player_points = yatzy_functions.get_all_points(players, "Player 1")
        print(f"Your points: {player_points}\nMinimum points: {minimum_points}")
        if player_points >= minimum_points:
            yatzy_functions.render_box("You won!")
        else:
            yatzy_functions.render_box("You lose...")
        print()

    else:

        yatzy_functions.render_table(players)
        
        score = [ [ player, yatzy_functions.get_all_points(players, player)] for player in players ]
        score = sorted(score, key = lambda element: element[1], reverse=True)
        all_points = [ player_points[1] for player_points in score]
        winner = max(all_points)
        if all_points.count(winner) > 1:
            winner_number = 1
            final_string = [ f"Draw between: {score[0][0]}" ]
            while winner_number < len(score) and score[winner_number][1] == score[0][1]:
                final_string += [ f", {players[score[winner_number][0]]["name"]}" ]
                winner_number += 1
            yatzy_functions.render_box(''.join(final_string))
            print()
        else:
            yatzy_functions.render_box(f"{players[score[0][0]]["name"]} is winner!")
            print()

    print("╧" * 100)


main()
