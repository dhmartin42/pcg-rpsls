play_choice = {
    'rock': 0,
    'spock': 1,
    'paper': 2,
    'lizard': 3,
    'scissors': 4,
}

player_choice = input("Please choose rock, paper, scissors, lizard, spock: ")
print(play_choice[player_choice])
print(list(play_choice.keys())[list(play_choice.values()).index(3)])