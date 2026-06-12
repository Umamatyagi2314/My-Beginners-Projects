import random

class Number_Guessing_Game: 
    def Guess_Number(self,user_name):
        attempt = 9
        count=0
        random_number = random.randint(1,100) # randomely choosen number

        while True:
            
            if (attempt == 0) and (user_choice != random_number):  # checks if all attempt has been completed and still random_choice not found then flag will declare as not found
                flag = "not found"
                break
            else:  # if attempts are left
                user_choice = int(input("Enter a number : "))
            count = count+1

            if user_choice == random_number:  # compare if user_choice equals to random_choice then declare flag as found 
                flag = "found"
                break
            elif user_choice > random_number:  # if user choice is greator then random number
                print(f"{user_choice} is too high ")
            elif user_choice < random_number:  # if user choice is smaller then random number
                print(f"{user_choice} too low ")
            

            attempt=attempt-1

        if flag == "found": # when number is guessed by the user
            print(f"\nRight guess : {user_choice}")
        elif flag == "not found":  # if failed all the attempts
            print(f"\nSorry {user_name} , you failed the game , (You can Try again or Leave) ")

        print(f"\nTotal Guess : {count}")  #how many attempts it takes to complete the game 

def main():
    print("Welcome to Number Guessing Game ")
    user_name = input("Enter your name : ")
    print(f"{user_name} you only have 9 attempts to win the game\n")
    Guess_num  = Number_Guessing_Game  # Object of Number_Guessing_Game class
    Guess_num.Guess_Number(user_name)

    while True:
        choice = input("\n\npress y/n for playing the game again : ")

        if choice == "y":
            print(f"\tReady to play again {user_name}\n")
            Guess_num.Guess_Number(user_name)
        else:
            print(f"Thankyou for playing with us {user_name}")
            break
            
if __name__ == "__main__":
    main()
