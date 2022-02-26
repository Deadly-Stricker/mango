import random as r
g=0
for i in range(0,100):
    a=r.randint(0,10)
    y=int(input("Enter a number between 0 and 10 (0 inclusive): "))
    if y==a:
        g=g+1
        print("You Guessed Right the answer was: ",a)
        print("You earned a guessing gem ,Your gems are: ",g)
        
    else:
        print("You guessed wrong, the answer was: ",a)
        print("Your gems count is: ",g)
        
