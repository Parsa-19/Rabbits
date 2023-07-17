import time
import random 


class Rabbits:

    def init(self):
        pass

    def generate_rab(self, dot, cloned_dot):
        
        lines = len(cloned_dot)
        select_line = random.randint(0, lines -1)

        if len(cloned_dot[select_line]) == 0:
            cloned_dot.pop(select_line)

        select_item = int(random.choice(cloned_dot[select_line]))      


        dot[select_line][select_item] = '   R   '
        cloned_dot[select_line].remove(select_item)

        # print(f"selected line is : {select_line}")
        # print(f"selected index is : {select_item}")
        # print(cloned_dot)
        return dot




# create list of dots with positions 
def create_dot_list(width, height):
    dot = []
    for h in range(height):
        dot_line = []
        for w in range(width):
            dot_line.append('   .   ')
        dot.append(dot_line)

    print("the list is successfully created!")
    return dot
'''
>>> input : 3
>>> input : 3
dot = [ ['x1', 'x2', 'x3'], ['x1', 'x2', 'x3'], ['x1', 'x2', 'x3'] ]
                             ---
>>> dot[1][0]
>>> output : x2
x2 in list 2
'''



# print map in the terminal
def print_map(dot):
    
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n')




rab = Rabbits()

height = int(input("height : "))
width = int(input("width : "))

dot = create_dot_list(width, height)

cloned_dot = []
for i in range(len(dot)):
    cloned_dot.append( list(range(0, len(dot[0]))) ) # it appends for example >> [0, 1, 2, 3]  



# counts days and provides map
num_of_days = 0 
while True:
    num_of_days += 1
    print(f"day{num_of_days}")

    rab.generate_rab(dot, cloned_dot)
    print_map(dot)
    time.sleep(1)