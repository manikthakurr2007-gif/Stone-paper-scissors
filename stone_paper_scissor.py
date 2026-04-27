import random
print("welcome to game")

def game():
    user_choice =input("enter your choice - (STONE , PAPER , SCISSOR ) : ").upper()
    elements = ["STONE","PAPER","SCISSOR"]


    if user_choice not in elements:
         user_choice = input("\ninvalid choice, please chosse correct option \n  (STONE , PAPER , SCISSOR ) :").upper()
 
    auto_choice = random.choice(elements)
    print("the computer choose - ",auto_choice)
    print("\nyou choose - ",user_choice)


    if auto_choice == user_choice :   
        print("\nmatch is tied ")
    elif (user_choice == "SCISSOR" and auto_choice == "PAPER" or user_choice == "STONE" and auto_choice == "SCISSOR"or user_choice == "PAPER" and auto_choice == "STONE"):
        print("congrats , you win")
    else:
        print("\nthe computer win \n you loss")

    x = input("\ndo you want to play game. (YES OR NO) :").upper()
    if x == "YES":
        game()
    elif x == "NO":
        print("\nthank you,for playing game")
    else:
        x = input("\ninvalid choice :(\ndo you want to play game. (YES OR NO) :").upper()
        if x == "YES":
            game()
        else:
             print("\nthank you , for playing")
game()