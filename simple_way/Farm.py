import time
import random
from replit import clear

class Rabbit:

    dot = []
    cloned_dot = {}
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
            cloned_keys = []
            for key in Rabbit.cloned_dot:
                cloned_keys.append(key)

    
            line = random.choice(cloned_keys)
            item = random.choice(Rabbit.cloned_dot[line]) 

            Rabbit.dot[line][item] = self.character
            Rabbit.cloned_dot[line].remove(item)
            print(f"line {line} item {item} is deleted")

            if len(Rabbit.cloned_dot[line]) == 0:
                '''
                remove the key
                '''
                Rabbit.cloned_dot.pop(line)



    def move(self):
        '''
        if nothing was in front then move on!
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


    @staticmethod
    def create_cloned_dot():
        for key in range(len(Rabbit.dot)):
            value_lst = []
            for value in range(len(Rabbit.dot[0])):
                value_lst.append(value)
            Rabbit.cloned_dot[key] = value_lst












def print_map(dot): 
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n' ,)

    


# create a list of dots and cloned_dot(with indexes)
out_of_range_rab = Rabbit()
out_of_range_rab.create_map() # I put the creation of dot list in Rabbit class because i needed the access of list inside class to replace, remove, move and.. the rabbits
out_of_range_rab.create_cloned_dot()

rab1 = Rabbit()



try :
    total_rab_objs = []
    i = 0
    while True:
        # clear()
        total_rab_objs.append(Rabbit()) # create rabbit and save it in total_rab_objs

        i += 1
        print(f"day : {i}")

        for rab in total_rab_objs:
            # rab.move()
            pass 
            
        
        print_map(Rabbit.dot)
        time.sleep(0.5)

except :
    def print_dict(dic):
        for i in dic:
            for j in dic[i]:
                print(j, end='      ')
            print('\n')
        
    print_dict(Rabbit.cloned_dot)