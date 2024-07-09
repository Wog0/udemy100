print("Welcome to Tresure Island")
print("Your mission is to find the treasure")

direction= input('You are at path that goes left or right, which path will you choose? Answer with "left" or "right" ').lower()

if direction == "left":
    swim= input('You come across a small pond, do you swim or do you wait. Type "swim" or "wait" ').lower()
    if swim == "wait":
        door= input('You come across three doors: one red, one yellow, and one blue. Which one do you choose? Type "red," "blue," or yellow" ').lower()
        if door == "yellow":
            print("You have found the treasure!")
        
        elif (door == "red") or (door =="blue"):
            print("You have died. Game over!")
        
        else:
            print("You have died. Game over!")

    else: 
        print("You have died. Game over!")


else:
    print("You have died. Game over!")