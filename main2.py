import random

# define the initial row of germs
germs = [1, 1, 1, 1, 1]

# print the initial row of germs
print(" ".join(str(g) for g in germs))

# play the game until all germs are eliminated
while sum(germs) > 0:
    # get user input for which germ to eliminate
    choice = input("Choose a germ to eliminate (1-5): ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > 5 or germs[int(choice)-1] == 0:
        choice = input("Invalid choice. Choose a germ to eliminate (1-5): ")
    choice = int(choice) - 1
    
    # eliminate the chosen germ
    germs[choice] = 0
    
    # spread the remaining germs
    for i in range(len(germs)):
        if germs[i] == 1:
            if i == 0:
                germs[i+1] = 0
            elif i == len(germs)-1:
                germs[i-1] = 0
            else:
                if random.random() < 0.5:
                    germs[i+1] = 0
                else:
                    germs[i-1] = 0
    
    # print the updated row of germs
    print(" ".join(str(g) for g in germs))

# print a message indicating that the game is over
print("Congratulations, you have eliminated all germs!")
