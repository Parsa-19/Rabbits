import time
import random
from replit import clear

class Rabbit:

    dot = []
    rab_tobe_count = 0

    def __init__(self):
        self.identity = Rabbit.rab_tobe_count    # .identity attribute tells you the index of specific rabbit you choosed4  # the first time its not actually a rabbit (out_of_range_rab = Rabbit)                                      
        self.character = '   R   '

        self.put() # put every rabbit one time when it's created 

        Rabbit.rab_tobe_count += 1
        



    # def empty_cells(self, dot):
    

    def put(self):
        '''
        choose random position between rest of empty cells
        '''
        if self.identity == 0 :
            return 0
        else :
            line = random.randint(0, len(Rabbit.dot)-1)
            item = random.randint(0, len(Rabbit.dot[0])-1) 

            Rabbit.dot[line][item] = self.character 



    def move(self):
        '''
        if nothing was in front then move
        ''' 
        line = random.randint(0, len(Rabbit.dot))
        item = random.randint(0, len(Rabbit.dot[0]))




    @staticmethod
    def create_map():
        for h in range(6): # 6 should be command (parameter)
            dot_line = []
            for w in range(6): # 6 should be command (parameter)
                dot_line.append('   .   ')
            Rabbit.dot.append(dot_line)
        print("the list is successfully created!")












def print_map(dot): 
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n' ,)

    


# create a list of dots at first
out_of_range_rab = Rabbit()
out_of_range_rab.create_map()


total_rab_objs = []
i = 0
while i < 10:
    clear()
    total_rab_objs.append(Rabbit()) # create rabbit and save it in total_rab_objs

    i += 1
    print(f"day : {i}")

    for rab in total_rab_objs:
        rab.move() 
        
    
    print_map(Rabbit.dot)
    time.sleep(1)

        