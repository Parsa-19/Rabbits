import time
import random
from replit import clear

class Rabbit:
    rab_tobe_count = 0

    def __init__(self):

        self.identity = Rabbit.rab_tobe_count
        self.character = '   R   '

        Rabbit.rab_tobe_count += 1




    # def display(self):
        

    # def empty_cells(self, dot):







def create_dot_list(width, height):
    dot = []
    for h in range(height):
        dot_line = []
        for w in range(width):
            dot_line.append('   .   ')
        dot.append(dot_line)

    print("the list is successfully created!")
    return dot

def print_map(dot): 
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n' ,)

# def delete_map(dot):
#     for h in range(len(dot)):
#         for w in dot[h]:
#             print('\r')
#         print('\n')
    





dot = create_dot_list(4, 4)
rab = Rabbit()

# i = 0
# while i < 10:
#     i += 1
#     print(f"day : {i}")

#     print_map(dot)
#     dot = rab.move(dot)
    
#     time.sleep(1)


total_rab_objs = []
i = 0
while i < 10:
    clear()

    i += 1
    print(f"day : {i}")

    total_rab_objs.append(Rabbit()) #rabbit is created in here
    for rab in total_rab_objs:
        # rab.display() # rabbit is shown in here
        # rab.move() 
        pass
    
    print_map(dot)
    time.sleep(1)

        