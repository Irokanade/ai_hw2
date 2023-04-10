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


def heuristic_func(state):
    germ_count = 0
    for germ in state:
        if germ == 1:
            germ_count += 1
    return germ_count

def ida_star_search(state, heuristic_func):
    threshold = heuristic_func(state)
    while True:
        result, new_threshold = search(state, 0, threshold, heuristic_func)
        print("current threshold: ", new_threshold)
        if result is not None:
            return result
        if new_threshold == float('inf'):
            return None
        threshold = new_threshold

def search(state, cost, threshold, heuristic_func):
    f = cost + heuristic_func(state)
    if f > threshold:
        return None, f
    if is_game_over(state):
        return [], cost
    min_cost = float('inf')
    for i in range(len(state)):
        new_state = state.copy()
        eliminate_germ(new_state, i)
        result, new_cost = search(new_state, cost+1, threshold, heuristic_func)
        if result is not None:
            result.insert(0, i)
            return result, new_cost
        if new_cost < min_cost:
            min_cost = new_cost
    return None, min_cost



fin = open("input.txt", "r")
fout = open("output.txt", "w")

lines = fin.readlines()

for line in lines:
    germs = []
    solution = ""
    # input_string = fin.read()
    germs = [int(x) for x in line.split(" ")]

    # print(germs)


    # perform iterative deepening search
    start_time = time.time()
    solution = ida_star_search(germs, heuristic_func)
    print("Total run time = %s seconds." % (time.time() - start_time))
    print("An optimal solution has " + str(len(solution)) + " moves.")
    print(" ".join(str(move+1) for move in solution))

    # write solution to file
    fout.write("Total run time = %s seconds.\n" % (time.time() - start_time))
    if solution is None:
        ("Total run time = %s seconds." % (time.time() - start_time))
        fout.write("There is no solution.\n")
    else:
        fout.write("An optimal solution has " + str(len(solution)) + " moves.\n")
        fout.write(" ".join(str(move+1) for move in solution))
        fout.write("\n")
        

fin.close()
fout.close()

# print(germs)