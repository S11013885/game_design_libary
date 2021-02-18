# dice roll library Amari Lombel, 2/18/2021,  12:23PM, version 0.1

# d4 simulator
def roll_d4(num_roll): #num_roll is an argument.
    import random
    
    rolls = 0
    while roll <= num_roll:
        result = random.randint(1,4)
        print (f" you rolled a {result} on the d4!n\")
        rolls += 1 
