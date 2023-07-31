import time
import random
from replit import clear
import sys, getopt

class Rabbit:

    dot = []
    cloned_dot = {}
    width = 0
    height = 0

    rab_tobe_count = 0
    line_rab = 0
    item_rab = 0
    

    def __init__(self):
        self.identity = Rabbit.rab_tobe_count    # .identity attribute tells you the index of specific rabbit you choosed4  # the first time its not actually a rabbit (out_of_range_rab = Rabbit)                                      
        self.character = '   R   '

        self.put() # put every rabbit just one time when it's created 

        Rabbit.rab_tobe_count += 1
        



    # def empty_cells(self, dot):

    ''' reason i defined a spwan function:
        to spwan any item including Rabbits, Carrots, Wolfs and... on map. so i created a function and pass the desired parametr as the character.
        i put this function in Rabbits class cause everything containing 'create dot_list, cloned_dots' and more are in here.
        then i will create class for carrots and wolfs and inhert them to Rabbit class. so they can access spwan func.
    '''
    def spawn(self, char): 
        cloned_keys = []
        for key in Rabbit.cloned_dot:
            cloned_keys.append(key)

        line = random.choice(cloned_keys)
        item = random.choice(Rabbit.cloned_dot[line]) 


        Rabbit.dot[line][item] = char
        Rabbit.cloned_dot[line].remove(item)
        print(f"item {self} spawn on -> line {line} item {item}")

        if len(Rabbit.cloned_dot[line]) == 0:
            '''
            remove the key
            '''
            Rabbit.cloned_dot.pop(line)

        return line, item



    def put(self):
        '''
        choose random position between rest of empty cells
        '''
        if self.identity == 0 :
            return 0
        else :
            line, item = self.spawn(self.character)

            #the initial assignment of rabbit position
            self.line_rab = line
            self.item_rab = item



    def move(self):
        '''
        if nothing was in front then move on!
        ''' 
        possible_moves = []

        pos = [self.line_rab, self.item_rab-1]
        possible_moves.append(pos)
        pos = [self.line_rab, self.item_rab+1]
        possible_moves.append(pos)

        pos = [self.line_rab-1, self.item_rab]
        possible_moves.append(pos)
        pos = [self.line_rab+1, self.item_rab]
        possible_moves.append(pos)
        

        for l, i in possible_moves:
            if Rabbit.dot[l][i] == '   .   ':
                '''
                put the rabbit in new position
                '''
                
    

 


    @staticmethod
    def create_map():
        for h in range(Rabbit.height):
            dot_line = []
            for w in range(Rabbit.width): 
                dot_line.append('   .   ')
            Rabbit.dot.append(dot_line)


    @staticmethod
    def create_cloned_dot():
        for key in range(len(Rabbit.dot)):
            value_lst = []
            for value in range(len(Rabbit.dot[0])):
                value_lst.append(value)
            Rabbit.cloned_dot[key] = value_lst


    @staticmethod
    def assign_dimentions(argv):
        # you can enter the dimention through option not argument:
        opts, args = getopt.getopt(argv, "w:h:i") # w=int(width), h=int(height), i:informations 
    
        for op, ar in opts: # ar is the argument that is related that option
            if op == '-i':
                print('''**********
usage:
    type -w following the desired width to apply the width
    and type -h following the desired height to apply the height
                      
syntax :
    -w <width> -h <height>

other options:
    -i : get help
**********''')
                print("press ctrl+C if you want yo keep this if not the game will start in :")
                i = 9
                while i != 0:
                    i -= 1
                    print(i, end='\r')
                    time.sleep(1)

            elif op in ('-w', '--width'):
                Rabbit.width = int(ar)
            elif op in ('-h', '--height'):
                Rabbit.height = int(ar)
        



class Carrot(Rabbit):

    def __init__(self):
        self.character = '   C   '

    def put(self):
        self.spawn(self.character)
            







        




def print_map(dot): 
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n' ,)

    









if __name__ == '__main__':

    # create a list of dots and cloned_dot(with indexes)
    out_of_range_rab = Rabbit()
    out_of_range_rab.assign_dimentions(sys.argv[1:])
    out_of_range_rab.create_map() # I put the creation of dot list in Rabbit class because i needed the access of list inside class to replace, remove, move and.. rabbits
    out_of_range_rab.create_cloned_dot()


    
    try :
        total_rab_objs = []
        i = 0
        while True:
            clear()
            total_rab_objs.append(Rabbit()) # create rabbit and save it in total_rab_objs
            car = Carrot()
            car.put()

            i += 1
            print(f"day : {i}")

            for rab in total_rab_objs:
                # rab.move()
                pass 
                
            
            print_map(Rabbit.dot)
            time.sleep(1)
    

    except :
        if len(Rabbit.cloned_dot) >= 1:
            print("\nempty dot indexes:")
            def print_dict(dic):
                for i in dic:
                    for j in dic[i]:
                        print(j, end='      ')
                    print('\n')
                
            print_dict(Rabbit.cloned_dot)
        else:
            print("DONE!")