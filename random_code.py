
def num ():
    while True:
        number = input("enter a number: ")
        if number.isdigit():
            number = int(number)
            break

        else:
            print("please enter a valid number")

    
    return number

        

def main():
    amount = num()
    




main()