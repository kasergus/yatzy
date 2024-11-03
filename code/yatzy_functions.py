import random
import points_functions

# generate_players: returns dictionary with players
def generate_players(amount):

    upper_section_names = [ "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes" ]

    # Creating dictionary with combination, which contains function for taking points and amount of points
    upper_section = { upper_section_combination_name: 
                        { 
                            "function": upper_section_combination_func,
                            "points": 0
                        } 
                    for upper_section_combination_name, upper_section_combination_func in zip(upper_section_names, points_functions.upper_section_combination_funcs) }

    lower_section = [ "One Pair", "Two Pairs", "Three Pairs", "Three of a Kind", "Four of a Kind", "Five of a Kind", "Full House", "Castle", "Tower", "Small Straight", "Large Straight", "Full Straight", "Chance", "Maxi Yatzy" ] 
    players = {} 

    # Creating players and adding combination with current dices to each
    for player_number in range(1, amount+1):
        players[f"Player {player_number}"] = dict.fromkeys(["Combinations", "Current dices"], 0)
        players[f"Player {player_number}"]["Combinations"] = { "Upper Section": upper_section, "Lower Section": lower_section }
        players[f"Player {player_number}"]["Current dices"] = []

    return players


# safe_int_input: avoids code breaking from wrong user input
def safe_int_input(bottom_limit=None, top_limit=None, message="Please, insert an integer"):

    # If user provided both limits
    userinput = bottom_limit - 1
    if bottom_limit and top_limit:
        while not(bottom_limit <= userinput <= top_limit):
            userinput = input(message)
            if not (userinput.isdigit() and bottom_limit <= int(userinput) <= top_limit):
                print(f"Please, insert an integer between {bottom_limit} and {top_limit}\n")
                userinput = bottom_limit - 1
            else:
                userinput = int(userinput)

    # If user provided only bottom_limit
    elif bottom_limit:
        while not(bottom_limit <= userinput):
            userinput = input(message)
            if not (userinput.isdigit() and bottom_limit <= int(userinput)):
                print(f"Please, insert an integer more or equal than {bottom_limit}")
                userinput = bottom_limit - 1
            else:
                userinput = int(userinput)

    # If user provided only top_limit
    elif top_limit:
        userinput = top_limit + 1
        while not(userinput <= top_limit):
            userinput = input(message)
            if not (userinput.isdigit() and int(userinput) <= top_limit):
                print(f"Please, insert an integer less or equal than {top_limit}")
                userinput = top_limit + 1
            else:
                userinput = int(userinput)

    # If user provided nothing
    else:
        userinput = input(message)
        while not userinput.isdigit():
            print("Please, insert an integer")
        userinput = int(userinput)

    return userinput

# get_dices: gets dices from user with possibility of reroll
def get_dices(dices_amount=6, maximum_rerolls=2):
    rerolls = maximum_rerolls
    dices = [ random.randint(1, 6) for _ in range (dices_amount) ]

    while rerolls > 0:
        print(f"Current dices: {dices}")
        print(f"You can reroll any amount of dices. Rerolls left: {rerolls}")
        indexes = []
        current_index = safe_int_input(0, dices_amount, f"Which of these dices you want to reroll? (print number of dice or 0 to stop)\n==> ")

        # Taking indexes of dices from user which he wants to reroll
        while len(indexes) < dices_amount and current_index:
            if current_index - 1 not in indexes:  # checking if user typing the same index
                indexes.append(current_index - 1)
            elif current_index:    
                print("You've already inserted this index")
            current_index = safe_int_input(0, dices_amount, "==> ")

        # Rerolling dices which user wants to reroll
        for index_of_dice_to_reroll in indexes:
            dices[index_of_dice_to_reroll] = random.randint(1, 6)
        
        # Stopping cycle if user didn't provide any index
        if len(indexes) == 0:
            rerolls = 0
        else:
            rerolls -= 1

    return dices
