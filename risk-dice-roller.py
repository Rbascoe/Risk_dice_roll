#risk-dice-roller
# from prompt_toolkit import prompt
import random


def battle_sim(attackers, stop_attack, defenders):

    while defenders >= 0 or (attackers >= stop_attack):
        #attacker rolls
        #Generate 5 random numbers between 0 and 7
        attacker_rolls = random.sample(range(1, 7), 3)
        # numbers.sort(reverse = True) => will sort the list of the attacker rolls from greatest to least
        attacker_rolls.sort(reverse= True)
        # print(attacker_rolls)
        

        #defender rolls 
        defender_rolls = random.sample(range(1, 7), 2)
        defender_rolls.sort(reverse= True)
        # print(defender_rolls)
        
                
        if(attacker_rolls[0] > defender_rolls[0]):
            defenders = defenders - 1
        elif((attacker_rolls[0] < defender_rolls[0]) or (attacker_rolls[0] == defender_rolls[0])):
            attackers = attackers - 1

        if(attacker_rolls[1] > defender_rolls[1]):
            defenders = defenders - 1  
        elif((attacker_rolls[1] < defender_rolls[1]) or (attacker_rolls[1] == defender_rolls[1])):
            attackers = attackers - 1
            
        #lose dice 
        if(attackers > 2):
            attacker_rolls.pop()
        elif(attackers == 1):
            attacker_rolls.pop()

           

    if(attackers <= 0 and defenders <= 0):
        print(attackers, defenders)
        print("We have a stalemate")

    if(defenders < 0 and attackers > defenders):
        defenders = 0
        if(defenders == 0):
            print(f"Attacker has won with {attackers} troops left!")

    if((attackers < 0 and defenders > attackers) and defenders > 0):
        print(attackers, defenders)
        attackers = 0
        if(attackers == 0):
            print(f"Defender has won with {defenders} troops left!")
    
    


def continue_playing():
    keep_playing = (input("Would you like to go again? "))
    keep_playing = keep_playing.lower()
    if(keep_playing == 'y'):
        start_game()
    elif(keep_playing == 'n'):
        print("See you later!")
    else:
        print("You have to pick y or n")
        continue_playing()


def start_game():
   
    #number of attacking units
    attackers = int(input("Number of attackers: "))
    #attack stop limit
    stop_attack = int(input("Stop attack when attaking troops reach: "))
    #number of defending units
    defenders = int(input("Number of defenders: "))

    print(battle_sim(attackers, stop_attack, defenders))
    
    continue_playing()

start_game()


