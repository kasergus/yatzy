# UPPER SECTION

# This function generates functions for all upper section combinatons
def generate_upper_section_combination_function(number):
    
    def sum_all_cubes(dices):
        
        return dices.count(number) * number

    # Returning a function, which returns sum of various numbers
    # a massive (user can pick which number function need to find and summarize)
    return sum_all_cubes



# LOWER SECTION

# duplicates: returns all duplicates in dices massive
def duplicates(dices):
    return [ dice for dice in dices if dices.count(dice) > 1 ]

# one_pair: retruns sum of one pair of the biggest duplicates
def one_pair(dices):
    return max(duplicates(dices) + [0]) * 2

# two_pairs: returns sum of two pairs of the biggest duplicates
# note: there is some variables for avoiding "magic numbers"
def two_pairs(dices):
    dices_duplicates = duplicates(dices) + [0]
    largest_duplicate = max(dices_duplicates)
    dices_duplicates_without_largest_duplicate = list(set(dices_duplicates) - {largest_duplicate} - {0}) + [0] 

    sum_of_first_pair = largest_duplicate * 2
    sum_of_second_pair = max(dices_duplicates_without_largest_duplicate) * 2

    return (sum_of_first_pair + sum_of_second_pair) * ((len(dices_duplicates_without_largest_duplicate) - 1) >= 1)  # multiplying by check if there is more than one pair 

# three_pairs: returns sum of three pairs of different duplicates
def three_pairs(dices):
    dices_duplicates = set(duplicates(dices))

    return sum(dices_duplicates) * 2 * (len(dices_duplicates) == 3)

# three_of_a_kind: returns sum of three biggest duplicates
def three_of_a_kind(dices):
    dices_duplicates = duplicates(dices)
    ordered_dices_duplicates = set(dices_duplicates)

    if not len(ordered_dices_duplicates):
        return 0

    return max(dices_duplicates) * 3 * ((len(dices_duplicates) / len(ordered_dices_duplicates)) != 2)  # multiplying by check if there is three same numbers
 
# four_of_a_kind: returns sum of four duplicates
def four_of_a_kind(dices):
    dices_duplicates = duplicates(dices)
    dices_duplicates_length = len(dices_duplicates)

    first_element_entries = dices_duplicates.count((dices_duplicates + [0])[0])
    third_element_entries = dices_duplicates.count((dices_duplicates + [0, 0, 0])[2])
    
    return max(dices_duplicates) * 4 * ( (dices_duplicates_length == 4 and first_element_entries == 4) or (dices_duplicates_length == 6 and (first_element_entries == 4 or third_element_entries == 4)) )   # multiplying by check if there is four same numbers

# five_of_a_kind: returns sum of five duplicates
def five_of_a_kind(dices):
    dices_duplicates = duplicates(dices) + [0]

    return max(dices_duplicates) * 5 * (dices_duplicates.count(dices_duplicates[0]) >= 5)  # multiplying by check if there is five (or more) same numbers 
# small_straight: returns 15 if there is 1, 2, 3, 4 and 5 in the dices
def small_straight(dices):
    return 15 * {1, 2, 3, 4, 5}.issubset(set(dices))

# large_straight: returns 20 if there is 2, 3, 4, 5 and 6 in the dices
def large_straight(dices):
    return 20 * {2, 3, 4, 5, 6}.issubset(set(dices))

# full_straight: returns 30 if all dices are different
def full_straight(dices):
    return 30 * (len(set(dices)) == 6)

# full_house: returns sum of combination of 3 duplicates of one type and 2 duplicates of another type
def full_house(dices):
    dices_duplicates = duplicates(dices)
    ordered_dices_duplicates = set(dices_duplicates)

    # check if there is more than five duplicates and remove if yes
    if len(dices_duplicates) == 6 and dices_duplicates.count(dices_duplicates[0]) == 3:
        dices_duplicates.remove(min(dices_duplicates))
    elif len(dices_duplicates) == 6:
        dices_duplicates.remove(max(dices_duplicates, key = dices_duplicates.count))

    return sum(dices_duplicates) * (len(dices_duplicates) == 5 and len(set(dices_duplicates)) == 2)

# castle: returns sum of all dices if there is 3 duplicates of one type and 3 duplicates of another type
def castle(dices):
    dices_duplicates = duplicates(dices)

    return sum(dices_duplicates) * (dices_duplicates.count((dices_duplicates + [0])[0]) == 3 and len(dices_duplicates) == 6)

# tower: returns sum of all dices if there is 4 duplicates of one type and 2 duplicates of another type 
def tower(dices):
    dices_duplicates = duplicates(dices)

    return sum(dices_duplicates) * (dices_duplicates.count((dices_duplicates + [0])[0]) != 3 and len(set(dices_duplicates)) == 2 and len(dices_duplicates) == 6)

# chance: returns sum of all dices
def chance(dices):
    return sum(dices)

# maxi_yatzy: returns 100 if all dices are same
def maxi_yatzy(dices):
    return 100 * (dices.count(dices[0]) == 6)



# Generating functions for upper section combinations
ones, twoes, threes, fours, fives, sixes = [ generate_upper_section_combination_function(number) for number in [1, 2, 3, 4, 5, 6]]


# Iinitializing massive with upper section functions
upper_section_combination_funcs = [ ones, twoes, threes, fours, fives, sixes ]

# Iinitializing massive with lower section functions
lower_section_combination_funcs = [ one_pair, two_pairs, three_pairs, three_of_a_kind, four_of_a_kind, five_of_a_kind, small_straight, large_straight, full_straight, full_house, castle, tower, chance, maxi_yatzy ]
