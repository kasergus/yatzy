import yatzy_functions 
import random

def main():

    # Variables for avoiding "magic" numbers
    player_limit = { "min": 1, "max": 6 }
    maximum_name_length = 8
    players_amount = 0
    dices_amount = 6
    players_amount = yatzy_functions.safe_int_input(player_limit["min"], player_limit["max"],  # Restrictions for amount of players
                                    f"How much players will play? (minimum is {player_limit["min"]}, maximum is {player_limit["max"]}): ")  # Message for user

    # Generating players
    players = yatzy_functions.generate_players(players_amount)

    # Getting all combinations blank for displaying 
    all_combinations = yatzy_functions.get_all_combinations(players)

    # Single player mode case
    if players_amount == 1:
        # Getting single player mode difficulty from user
        print("\nSingle player. Pick mode:\n1. Easy\n2. Medium\n3. Hard")
        mode = yatzy_functions.safe_int_input(1, 3, "\n==> ")
        # Getting minimum points limit, which user must get to win (limit depends on mode)
        minimum_points = [random.randint(50, 150), random.randint(150, 250), random.randint(250, 350)][mode-1]

    # Main game cycle: getting dices from user(s) and
    # crossing or giving points for combinations
    game_over = False
    while not game_over:
        for player in players:

            # If player don't have any available combinations - skipping him
            if not players[player]["available"]:
                continue
    
            # Printing for user which turn to play
            print("\n" * 2 + "═" * 100)
            yatzy_functions.render_box(f"{players[player]["name"]}, your turn!")

            # Printing user score sheet
            print("═" * 100)
            print("Your score sheet:")
            yatzy_functions.render_score_sheet(players, player)
            print("═" * 100 + "\n")

            dices = yatzy_functions.get_dices()   

            # Printing user his dices
            players[player]["current dices"] = dices[:]  # Added [:] to create a new massive
            print("\n" + "═" * 100)
            yatzy_functions.render_box(f"Your dices: {dices}") 
            print("═" * 100)

            # Getting all unused and available combinations
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
    
            # If there is at least one available combination for current dices -
            # letting user choose from which he wants to earn points (or pick 0 if he wants to cross)
            if len(available_combinations):    
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

            # If there is no available combinations - user choosing to cross automaticly 
            else:
                user_choice = 0
                print("There is no available combinations for your dices :(\n")



            # Crossing combination if user choosed it (or if there is no available combinations)
            if not (len(available_combinations) and user_choice):
                print("Your unused combinations:\n")
                for combination_number in unused_combinations:
                    print(f"{combination_number}. {unused_combinations[combination_number]["combination"]}")
                user_choice = yatzy_functions.safe_int_input(1, unused_combination_number, "Pick which combination you want to cross\n✖ ")
                section = unused_combinations[user_choice]["section"]
                combination = unused_combinations[user_choice]["combination"]
                players[player]["combinations"][section][combination]["points"] = 0

            # In other case, giving points to combination, which user picked
            else:
                section = available_combinations[user_choice]["section"]
                combination = available_combinations[user_choice]["combination"]
                players[player]["combinations"][section][combination]["points"] = players[player]["combinations"][section][combination]["function"](dices)
    
            # If user don't have any combinations to use - making him unavailable
            if len(unused_combinations) - 1 == 0:
                players[player]["available"] = False

        # game_over: will be true only if all users are unavailable
        game_over = set([players[f"Player {player_number}"]["available"] for player_number in range(1, players_amount + 1)]) == {0}


    # Separators for nicer view
    print("\n" * 10)
    print("╤" * 100 + "\n")

    # If there is only one player - printing if he won or loosed
    if players_amount == 1:
        player_points = yatzy_functions.get_all_points(players, "Player 1")
        print(f"Your points: {player_points}\nMinimum points: {minimum_points}")
        if player_points >= minimum_points:
            yatzy_functions.render_box("You won!")
        else:
            yatzy_functions.render_box("You lose...")
        print()

    # If there is more than one player - printing winner(s)
    else:

        yatzy_functions.render_players_table(players)
        
        # Getting all points from all users and sorting points
        score = [ [ player, yatzy_functions.get_all_points(players, player)] for player in players ]
        score = sorted(score, key = lambda element: element[1], reverse=True)

        # Finding winner
        all_points = [ player_points[1] for player_points in score]
        winner = max(all_points)

        # If there is more than one winner - printing draw between all of them
        if all_points.count(winner) > 1:
            winner_number = 1
            final_string = [ f"Draw between: {score[0][0]}" ]
            while winner_number < len(score) and score[winner_number][1] == score[0][1]:
                final_string += [ f", {players[score[winner_number][0]]["name"]}" ]
                winner_number += 1
            yatzy_functions.render_box(''.join(final_string))
            print()

        # If there is only one winner - printing that he won (finally)
        else:
            yatzy_functions.render_box(f"{players[score[0][0]]["name"]} is winner!")
            print()

    print("╧" * 100)

main()
