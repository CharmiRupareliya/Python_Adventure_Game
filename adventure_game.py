import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print()
name  = input("Please Enter your name : ")

print(Fore.MAGENTA + Style.BRIGHT + f"Welcome {name} to this adventure!\U0001F30F")
print()
ans = input("You are on dirt road, it has come to an end & you can go left or right. Which way would you like to go (left/right)? : ").lower()

if ans == "left":
    ans = input("You come to river, you can walk around it & swim accross (walk/swim)? : ").lower()

    if ans == "swim":
        print("You Swam accross and Congratulations! You found the Treasure Chest and won the game! ")
    elif ans == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print(Fore.RED + "Not valid data. Yoy Lost the Game....")


elif ans == "right":
    ans = input("You come to a bridge🌉, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if ans == "back":
        print("You go back and You Lost the Game....")
    elif ans == "cross":
        ans = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if ans == "yes":
            print("You talk to the stanger and they give you gold\U0001F4B0. You WIN! ")
        elif ans == "no":
            print("You ignore the stranger and they are offended and You Lost the Game.... ")
        else:
            print(Fore.RED + "Not valid data. You Lost the Game....")
    else:
        print(Fore.RED + "Not valid data. You Lost the Game....")

else:
    print(Fore.RED + 'Not a valid option. You lose.')

print()
print(Fore.CYAN + Style.BRIGHT + f"Thank you for Playing,{name}")
