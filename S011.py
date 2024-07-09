import random




# while difficulty != "h" or "e":
#     print("you did not choose a correct option")
#     difficulty = input('Type "h" to play on mode or "e" to play on easy mode: ')



def compare(guessing, answering):
    if guessing < answering:
        print(("Your guess is too low"))
    
    elif guessing > answering:
        print(("your guess is too high"))

    else:
        print(("You are correct!"))




def easy_hard(difficulty):
    easy_mode = 10
    hard_mode = 5
    if difficulty == "easy":
        return easy_mode
    elif difficulty == "hard":
        return hard_mode

 

 
def randonum():

    my_list = []
    for i in range (1, 101):
        my_list.append(i)
     
    return random.choice(my_list)



def game():
    gaming = True
    answer = randonum()
    print(answer)
    difficulty = input("do you want to play on easy or hard mode: ")
    lives = easy_hard(difficulty)
    
    while gaming: 
        print(lives)
        guess = int(input("guess a number between 1 and 100\n"))
        compare(guessing = guess, answering = answer)
        if guess == answer:
            new_game = input("would you like to start a new game?")
            if new_game == "yes":
                game()
            
            else:
                gaming = False
        
        else:
            lives = lives -1
            if lives == 0:
                print("You have lost")
                gaming = False

    
        
            
    
            
           
                
            


   

while input("Do you want to play higher or lower?\n").lower() == "yes":
    game()


        



   







    





 

