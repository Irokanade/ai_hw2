# function to mutate the viruses
def mutate(germ_list):
    tempList = [0]

    for i in range(len(germ_list)):
        if(germ_list[i] == 1):
            # do left side
            if(i > 0):
                tempList[i-1] = tempList[i-1] or 1

            # middle
            tempList[i] = tempList[i] or 0

            # do right side
            if(i < len(germ_list)-1):
                tempList.append(1)

        elif(i < len(germ_list)-1):
            # if 0 do nothing add 0 to right side
            tempList.append(0)

        # print(tempList)

    # print(tempList)
    # set tempList to germ_list
    for i in range(len(tempList)):
        germ_list[i] = tempList[i]

# function to eliminate germ given position
def eliminate_germ(germ_list, i):
    germ_list[i-1] = 0


germs = []
solution = ""

fin = open("input.txt", "r")
fout = open("output.txt", "w")

inputString = fin.read()
germs = [int(x) for x in inputString.split(" ")]

print(germs)

eliminate_germ(germs, 4)
print(germs)
mutate(germs)
print(germs)

eliminate_germ(germs, 3)
print(germs)
mutate(germs)
print(germs)

eliminate_germ(germs, 5)
print(germs)
mutate(germs)
print(germs)

fout.write(solution)

fin.close()
fout.close()

print(germs)