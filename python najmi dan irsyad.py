import random

def main():
    """#guess element in pariodict table"""
    print("welcome to our guessing game")
    list=("hidrogen","nitrogen","oksigen","helium")
    x = random.choice(list)
    guess = None
    
    while x !=guess:
        
        guess = str(input("pick any element hidrogen,nitrogen,oksigen,helium:"))
                    
        if x == guess:
            print("congratulations")
        elif x > guess:
            print("try another element.")
        elif x > guess:
            print("try a another element.")

main()