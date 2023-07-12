import time
import random 


class Rabbits:

    def __init__(self):
        pass

    def print_R(self, dot):
        #it has to be done just  for one time
        cloned_dot = []
        for i in range(len(dot)):
            cloned_dot.append( list(range(0, len(dot[0]))) )
        print(cloned_dot)

        line = len(dot)
        item = len(dot[0])
        select_line = random.randint(0, line-1)
        select_item = random.randint(0, item-1)       

        if dot[select_line][select_item] != '   R   ':
            dot[select_line][select_item] = '   R   '
                
        return dot




        
        


# create list of dots with positions 
def create_dot_list(width, height):
    dot = []
    for h in range(height):
        dot_line = []
        for w in range(width):
            dot_line.append('   .   ')
        dot.append(dot_line)

    return dot


# print map in the terminal
def print_map(dot):
    
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n')







height = int(input("height : "))
width = int(input("width : "))
#1:
dot = create_dot_list(width, height)

rab_1 = Rabbits()
rab_1.print_R(dot)


# counts days and provides map
# num_of_days = 0 
# while num_of_days < 10:
#     num_of_days += 1

#     print(f"index = {num_of_days}")
#     dot = rab_1.print_R(dot)
#     #2:
#     print_map(dot)
#     time.sleep(1)





