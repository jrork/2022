
score_key = [[3,6,0],[0,3,6],[6,0,3]]
score_key_index = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
name = {'A':'Rock', 'B':'Paper', 'C':'Scissors', 'X':'Rock', 'Y':'Paper', 'Z':'Scissors'}
choice_value = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
outcome_key = [['C', 'A', 'B'],['A', 'B', 'C'],['B', 'C', 'A']]
outcome_key_index = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

# the second column says how the round needs to end: X means you need to lose, 
# Y means you need to end the round in a draw, and Z means you need to win

def main():
    total_score = 0
    round_number = 0
    file = open("RPS.data")

    while True:
        round = file.readline()
        if not round:
            break
        round_number = round_number + 1
        print(f"Round #:{round_number}")
        opponent_choice = round[0]
        outcome = round[2]
        my_choice = get_my_choice(opponent_choice, outcome)
        round_score = get_round_score(opponent_choice, my_choice)
        total_score = get_total_score(total_score, round_score, my_choice)
        print()
    file.close()

def get_my_choice(opponent_choice, outcome):
    opponent_choice_index = outcome_key_index[opponent_choice]
    outcome_index = outcome_key_index[outcome]
    my_choice = outcome_key[opponent_choice_index][outcome_index]
    return my_choice

def get_round_score(opponent_choice, my_choice):
    score = score_key[score_key_index[opponent_choice]][score_key_index[my_choice]]
    print(f"{name[opponent_choice]}({opponent_choice}) vs. {name[my_choice]}({my_choice}): {score}")
    return score

def get_total_score(total_score, round_score, choice):
    choice_score = choice_value[choice]
    total_score = total_score + round_score + choice_score
    print(f"Round score: {round_score}, Choice score: {choice_score}, Total score: {total_score}")
    return total_score

if __name__ == "__main__":
    main()