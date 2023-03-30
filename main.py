import time

# function to mutate the viruses
def mutate(germ_list):
    temp_list = [0]

    for i in range(len(germ_list)):
        if(germ_list[i] == 1):
            # do left side
            if(i > 0):
                temp_list[i-1] = temp_list[i-1] or 1

            # middle
            temp_list[i] = temp_list[i] or 0

            # do right side
            if(i < len(germ_list)-1):
                temp_list.append(1)

        elif(i < len(germ_list)-1):
            # if 0 do nothing add 0 to right side
            temp_list.append(0)

        # print(temp_list)

    # print(temp_list)
    # set tempList to germ_list
    for i in range(len(temp_list)):
        germ_list[i] = temp_list[i]

# function to eliminate germ given position
def eliminate_germ(germ_list, i):
    germ_list[i] = 0
    mutate(germ_list)

def is_game_over(germ_list):
    for germ in germ_list:
        if(germ == 1):
            return False

    return True


# iterative deepening search function
def search(germs):
    for depth in range(1, len(germs)**2):
        print("searching at depth", depth)
        solution = depth_limited_search(germs, depth)
        if solution is not None:
            return solution
    return None

# depth-limited search function
def depth_limited_search(germs, depth):
    if is_game_over(germs):
        return []
    elif depth == 0:
        return None
    else:
        for move in range(len(germs)):
            new_germs = germs[:]
            eliminate_germ(new_germs, move)

            # print(new_germs)
            result = depth_limited_search(new_germs, depth-1)
            if result is not None:
                return [move] + result
        return None


germs = []
solution = ""

fin = open("input.txt", "r")

input_string = fin.read()
germs = [int(x) for x in input_string.split(" ")]

# print(germs)
# for i in range(3):
#     temp = germs[:]
#     eliminate_germ(temp, i)
#     print(temp)

# eliminate_germ(germs, 2)
print(germs)


# perform iterative deepening search
start_time = time.time()
solution = search(germs)
print("Total run time = %s seconds." % (time.time() - start_time))

# write solution to file
with open("output.txt", "w") as fout:
    if solution is None:
        fout.write("There is no solution.")
    else:
        fout.write(" ".join(str(move+1) for move in solution))

fin.close()
fout.close()

# print(germs)