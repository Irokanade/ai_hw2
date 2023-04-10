import random

def generate_input(file_name):
    f = open(file_name, "w")
    germ_list = []
    num_germs = random.randint(1, 60)
    for j in range(num_germs):
        germ_list.append(random.randint(0, 1))
    # print(" ".join(str(x) for x in germ_list))
    f.write(" ".join(str(x) for x in germ_list) + "\n")   

    f.close()


generate_input("input0.txt")
generate_input("input1.txt")
generate_input("input2.txt")
generate_input("input3.txt")
generate_input("input4.txt")