import sys        # for sys.exit
import random     # for randrange

###################################################
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
##################################################

choice = {
    'rock': 0,
    'spock': 1,
    'paper': 2,
    'lizard': 3,
    'scissors': 4,
}

player_win_count = 0
comp_win_count = 0

def rpsls(player_choice): 
    """ 
       rpsls:
       Parameter: player_choice: string - rock, paper, scissors, lizard, spock
       This function assigns the player choice and uses modulus to figure out who 
       won the game. 
    """
    player_number = choice[player_choice.lower()]
    comp_number = random.randrange(0,5)

    global player_win_count
    global comp_win_count
    
    # performs modulus step to determine the winner
    modulo_step = (int(comp_number) - int(player_number)) % 5
        
    # this gets the name from the number, using a little dictionary voodoo
    print ()
    print ("Player chose: " + list(choice.keys())[list(choice.values()).index(player_number)])
    print ("Computer Chose: " + list(choice.keys())[list(choice.values()).index(comp_number)])
    
    
    # I compare first the tie scenario then the computer
    # win and then the player win. 
    # 0 == tie, 1 or 2 == computer wins, 3 or 4 == player wins
    if (modulo_step == 0):
        player_win_count += 1
        comp_win_count += 1
        print ("Player and Computer Tie! Computer: "+ str(comp_win_count) + " Player: " + str(player_win_count))
    elif(modulo_step == 1 or modulo_step == 2):
        comp_win_count += 1
        print ("Computer Wins! Computer: "+ str(comp_win_count) + " Player: " + str(player_win_count))
        
    elif(modulo_step == 3 or modulo_step == 4):
        player_win_count +=1
        print ("Player Wins! Computer: "+ str(comp_win_count) + " Player: " + str(player_win_count))
        
    else: 
        print ("whoops! you are not supposed to see this.")

def help():
    print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, \nlizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")

def quit():
    print ("Thanks for playing! You got "+ str(player_win_count) + " The computer got " + str(comp_win_count))
    sys.exit()

def main():
    # main game loop, infinite loops for the win! 
    while (True): 
        
        player_choice = input("Please enter rock, paper, scissors, lizard or spock. If You want the rules, type help, if you don't want to play type quit: ")

        if (player_choice.lower() == 'rock') \
            or (player_choice.lower() == 'paper') \
            or (player_choice.lower() == 'scissors') \
            or (player_choice.lower() == 'lizard') \
            or (player_choice.lower() == 'spock'): 

            rpsls(player_choice)

        elif (player_choice.lower() == 'help'):
            help()

        elif (player_choice.lower() == 'quit'):
            quit()

if __name__ == "__main__":
    main()