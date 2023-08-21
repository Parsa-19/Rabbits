'''
execution >>> python3 file_name.py 5 7 0.8
first option (5) : map_width
second option (7) : map_height
third option (0.8) : how long the day would take in second


W = adult Wolf
w = child wolf
R = adult Rabbit
r = child rabbit
C = healthy Carrot
c = rotten carrot


W > R    +100  | feed wolf 
R > C    +100  | feed rabbit
R > c    -75   | reduce_rabbit_health
W,R > .  -50   | (empty cell)  reduce_creature_health 
'''


import time
import random 
import getopt
import os, sys

class Creature:

    def __init__(self, char, age='adult', sick=False):
        self.char = char
        self.coor = ()
        self.health = 100
        self.gender = random.choice(['Male', 'Female'])
        self.stomach = []
        self.age = age
        self.sick = sick
    


class Wolf(Creature):
    temp_map = []
    cuple_found = 0
    baby_generated = 0
    def __init__(self, char, age='adult', sick=False):
        super().__init__(char, age='adult')

class Rabbit(Creature):
    temp_map = []
    cuple_found = 0
    baby_generated = 0
    def __init__(self, char, age='adult', sick=False):
        super().__init__(char, age, sick)

class Carrot:
    temp_map  = []
    def __init__(self, char):
        self.char = char
        self.coor = ()
        self.state = random.choice([True, True, True, True, False])





class Gameplay:
    map = []
    total_car, total_rab, total_wol = [], [], []
    items_cls = [Wolf, Rabbit, Carrot]
    temp = {} # to get all of class'es temp maps

    cuple_found = 0
    baby_generated = 0

    for cls in items_cls:
        temp[cls] = cls.temp_map 
        

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_map(self):
        for x in range(self.height):
            line_append = []
            for y in range(self.width):
                line_append.append('  .  ')
            Gameplay.map.append(line_append)

    def print_map(self):
        for x in range(len(Gameplay.map)):
           for y in range(len(Gameplay.map[x])):
               print(Gameplay.map[x][y], end = '')
           print('\n')

    def create_temp_map(self, cls):
        for x in range(len(Gameplay.map)):
            line_append = []
            for y in range(len(Gameplay.map[0])):
                line_append.append((x, y))
            cls.temp_map.append(line_append)
    
    def print_temp_map(self, cls):
        # i = len(cls.temp_map) - 1
        for x in range(len(Gameplay.map)):
            for y in range(len(Gameplay.map[0])):
                print(cls.temp_map[x][y], end='')
                # print(cls.temp_map[i], end='-')
                # i -= 1
            print('\n')
####################################################################################################################################



    def apply_obj_on_pre_temp(self, type, coor):  # apllies the object on its previous temp map (every items that exist in the map, has their own temp_map) oeder : Wolf > Rabbit > Carrot
        
        def put(pre_cls, foodChar, total_objs): # put_on_pre_temp_map and check if its replacing with food or not 

            if Gameplay.temp[pre_cls][coor[0]][coor[1]] == foodChar:  # if there is food in where object is going to spawn then: (1.2.3)
                for food_obj in total_objs: # find the food
                    if food_obj.coor == (coor[0], coor[1]):
                        # 1.feed the type_obj
                        self.feed(type, food_obj)
                        # 2.remove the cloned char of food obj in its pre_temp
                        if pre_cls == Rabbit:
                            Gameplay.temp[Carrot][coor[0]][coor[1]] = coor
                        elif pre_cls == Carrot:
                            Gameplay.temp[Wolf][coor[0]][coor[1]] = coor
                        # 3.remove the food
                        total_objs.remove(food_obj)
                        del food_obj
                        break
            else: # if there is nothing in where object is going to spawn then reduce_health
                self.reduce_health(type)

            if len(type.coor) > 0 : # this will execute when apply function is called by move (they have coor attr filled, when they want to move) 
                Gameplay.temp[pre_cls][type.coor[0]][type.coor[1]] = type.coor  # type.coor is the last pos; and coor(in next line) is the new pos
            Gameplay.temp[pre_cls][coor[0]][coor[1]] = type.char

        if isinstance(type, Wolf):
            put(Rabbit, '  R  ', Gameplay.total_rab) # you need to pass the specification of the previouse temp map
            Gameplay.temp[Carrot][type.coor[0]][type.coor[1]] = type.coor
            Gameplay.temp[Carrot][coor[0]][coor[1]] = type.char # exception: the wolf would be put himself in carrot temp too (so carrots can't eat wolf)
        elif isinstance(type, Rabbit):
            put(Carrot, '  C  ', Gameplay.total_car)
        elif isinstance(type, Carrot):
            Gameplay.temp[Wolf][coor[0]][coor[1]] = type.char

            



    def spawn(self, type, coordinate=None):
        if coordinate:
            x, y = coordinate
        else:
            # find the empty cells
            empt_cells = []
            for line in Gameplay.temp[type.__class__]:
                for cell in line:
                    if isinstance(cell, tuple):
                        empt_cells.append(cell)
            # choose a random coordiante between empty cells 
            x, y = random.choice(empt_cells)
                
        Gameplay.map[x][y] = type.char
        type.coor = (x, y)

        Gameplay.temp[type.__class__][x][y] = type.char
        self.apply_obj_on_pre_temp(type, (x, y))  # in progress 




    def feed(self, type, food_obj):
        hp = 100
        if food_obj.char == '  C  ':
            if food_obj.state == False:
                hp = -75      
        type.health += hp
        type.stomach.append(food_obj)
    
    def reduce_health(slef, type):
        decr_amount = -50 # decrease_amount

        if not type.sick: # not zero returns True 
            decr_amount = decr_amount*3 
            
        type.health += decr_amount




    def get_around(self, type):
        curr_x, curr_y = type.coor # current x and current y
        all_around = [(curr_x, curr_y-1), (curr_x, curr_y+1),
                  (curr_x-1, curr_y), (curr_x+1, curr_y)]
        
        possible_around = []
        for x, y in all_around:
            if x >= 0 and x < len(Gameplay.map[0]) and y >= 0 and y < len(Gameplay.map): # if the cell's coordinate was in map;
                possible_around.append((x, y))

        return possible_around
    


    def move(self, type):
        possible_moves = self.get_around(type)

        while possible_moves:
            new_coor = random.choice(possible_moves)

            for line in Gameplay.temp[type.__class__]:
                if new_coor in line:
                    Gameplay.map[type.coor[0]][type.coor[1]] = '  .  '
                    Gameplay.map[new_coor[0]][new_coor[1]] = type.char
                    Gameplay.temp[type.__class__][type.coor[0]][type.coor[1]] = type.coor
                    Gameplay.temp[type.__class__][new_coor[0]][new_coor[1]] = type.char
                    self.apply_obj_on_pre_temp(type, new_coor)
                    type.coor = new_coor
                    break

            else :
                possible_moves.remove(new_coor)
                continue
            break


    
    def check_partner(self, type):
        around_cells = self.get_around(type)

        for x, y in around_cells:
            for rab_ins in Gameplay.total_rab:
                if rab_ins.coor == (x, y) and rab_ins.gender == "Female" and rab_ins.age == 'adult':
                        return True  
        return False
    

    def generate_item(self, type, cls, baby_char):
        around_cells = self.get_around(type)

        while around_cells:
            x, y = random.choice(around_cells)
            for line in Gameplay.temp[type.__class__]:
                if (x, y) in line:
                    baby = cls(baby_char, age='baby', sick=random.choice([i for i in range(0, 10)]))
                    self.spawn(baby, (x, y))
                    return baby
            else:
                around_cells.remove((x, y))

            
        return None # return none when there is no place to generate new rab




        

    def show_item_info(self, cls, objects):
        print(cls.__name__, ":")
        for obj in objects:
            print(f"{obj.char}({obj.gender}) health is--> {obj.health} | ate: {[item.char for item in obj.stomach]}")



        





############ desierd arguments ############
width, height = 4, 4
day_distance = 1 # sec
args = sys.argv[1:]
if len(args) >= 2:
    if len(args) == 3 :
        day_distance = args[2]
    width, height = int(args[0]), int(args[1])
############ desierd arguments ############



############ initial stuff ############
game = Gameplay(width, height)
game.create_map()
for cls in Gameplay.items_cls: # create items temp map
    game.create_temp_map(cls)
############ initial stuff ############




try:
    if __name__ == '__main__':




        
        day_count = 1
        break_out = True
        while True:
            print(f"\nday {day_count}:")
 
            car = Carrot('  C  ')
            Gameplay.total_car.append(car)
            game.spawn(car)


            rab = Rabbit('  R  ') 
            Gameplay.total_rab.append(rab)
            game.spawn(rab)
            for rab in Gameplay.total_rab:
                game.move(rab)  
                if rab.age == 'adult' and rab.gender == 'Male':
                    in_love = game.check_partner(rab)
                    if in_love == True:
                        Rabbit.cuple_found += 1
                        baby_rab = game.generate_item(rab, Rabbit, '  r  ') # need the father's rab obj, class and the character
                        if baby_rab: # if baby_rab is containing a rab object in it, now it can take place in total_rabs
                            Gameplay.total_rab.append(baby_rab)
                            Rabbit.baby_generated += 1


            wol = Wolf('  W  ')
            Gameplay.total_wol.append(wol)
            game.spawn(wol)
            for wol in Gameplay.total_wol:
                game.move(wol)
                if wol.age == 'adult' and wol.gender == 'Male':
                    in_love = game.check_partner(wol)
                    if in_love == True:
                        Wolf.cuple_found += 1
                        baby_wol = game.generate_item(wol, Wolf, '  w  ') # need the father's rab obj, class and the character
                        if baby_wol: # if baby_wol is containing a wol object in it, now it can take place in total_rabs
                            Gameplay.total_wol.append(baby_wol)
                            Wolf.baby_generated += 1


            game.print_map()

            # print('---------------------')
            # game.print_temp_map(Carrot)
            # print('---------------------')
            # game.print_temp_map(Rabbit)
            # print('---------------------')
            # game.print_temp_map(Wolf)

            
            
                

            time.sleep(float(day_distance))
            day_count += 1

    print("Done!")
except KeyboardInterrupt:
    print('\nthis is the exception:::: \n')
    print('Wolf temp map:\n')
    game.print_temp_map(Wolf)
    print('Rabbit temp map:\n')
    game.print_temp_map(Rabbit)
    print('Carrot temp map:\n')
    game.print_temp_map(Carrot)



    # print("Rabbits got {} marriage. and {} babies".format(Rabbit.cuple_found, Rabbit.baby_generated))
    # print("Wolfs got {} marriage. and {} babies".format(Wolf.cuple_found, Wolf.baby_generated))
    # print('\n')
    
    # game.show_item_info(Rabbit, Gameplay.total_rab)
    # game.show_item_info(Wolf, Gameplay.total_wol)






