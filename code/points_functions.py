
# This function generates functions for all upper section combinatons
def generate_upper_section_combination_function(number):
    
    def sum_all_cubes(dices):
        
        return dices.count(number) * number

    # Returning a function, which returns sum of various numbers
    # a massive (user can pick which number function need to find and summarize)
    return sum_all_cubes


# Initializing functions for upper section combinations
ones, twoes, threes, fours, fives, sixes = [ generate_upper_section_combination_function(number) for number in [1, 2, 3, 4, 5, 6]]

# Generating massive with upper section functions
upper_section_combination_funcs = [ ones, twoes, threes, fours, fives, sixes ]
