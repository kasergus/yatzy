import yatzy_functions 

def main():

    # Variables for avoiding "magic" numbers
    player_limit = { "min": 2, "max": 6 }
    maximum_rerolls = 2
    players_amount = 0
    dices_amount = 6
    
    players_amount = yatzy_functions.safe_int_input(player_limit["min"], player_limit["max"],  # Restrictions for amount of players
                                    f"How much players will play? (minimum is {player_limit["min"]}, maximum is {player_limit["max"]}): ")  # Message for user

    players = yatzy_functions.generate_players(players_amount)

    for player in players:

        print(100 * '-')
        print(f"{player}, your turn!")

        rerolls = maximum_rerolls
        dices = yatzy_functions.get_dices()   
        players[player]["Current dices"] = dices[:]  # Added [:] to create a new massive

        print("Current dices ---:", dices)
        print("Current player:", players[player])

main()
