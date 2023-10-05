import random
import sys
import os
import time

class Creature:
    def __init__(self, char):
        self.char = char 
        self.coor = ()


class rabbit(Creature):
    def __init__(self, char):
        super().__init__(char)


class wolf(Creature):
    def __init__(self, char):
        super().__init__(char)


class carrot:
    def __init__(self, char):
        self.char = char


class GamePlay:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [['  .  ' for w in range(self.width)] for h in range(self.height)]
        self.all_map_coors = [item for row in [[(h, w) for w in range(len(self.map[h]))] for h in range(len(self.map))] for item in row] # this var includes all the map coordinates 
        self.food_for = {
            '  C  ':'',
            '  R  ':'  C  ',
            '  W  ':'  R  '
        }       

    def print_day(self):
        for h_index in range(self.height): # height_index 
            for w_index in range(self.width): # weight_index
                print(self.map[h_index][w_index], end='')
            print('\n')

    
    def feed(self, type, spawn_x, spawn_y):
         obj_lst_handler = {
                '  C  ': carrot_objs,
                '  R  ': rabbit_objs,
                '  W  ': wolf_objs
                } 
         for food_obj in obj_lst_handler[self.food_for[type.char]]:
            if food_obj.coor == (spawn_x, spawn_y):
                obj_lst_handler[self.food_for[type.char]].remove(food_obj)
                try : 
                    del food_obj
                    
                except :
                    print('couldnt deleted the food !')



    def get_empty_cells(self, type, is_around=False):
        # var 'map_coordinates' use all the map coordinates by default when functions starts
        map_coordinates = self.all_map_coors

        def set_around_cells():
            x, y = type.coor
            moves = [(x, y-1), (x, y+1), # this will cause an error if you call this functions through the spawn method by attribute (is_around = True)
                     (x-1, y), (x+1, y)] # because there is no coordinate before you spawn the item with no is_around
                                         # so dont try >>> get_empty_cells(is_around=True) in spawn method
            around = []
            for cell in moves:
                if cell in self.all_map_coors:
                    around.append(cell)
            return around
        # if you just want all around empty coordiantes then 'map_coordinate' will be what you wanted'
        if is_around: 
            map_coordinates = set_around_cells()
            
                
        cell_types = ['  .  '] # we check which cells counts as empty by this variable

        def set_rabbits_empty_cells():
            cell_types.append('  C  ')

        def set_wolfs_empty_cells():
            cell_types.append('  R  ')
        
        def set_carrot_empty_cells():
            pass

        func_handle = {
            '  R  ' : set_rabbits_empty_cells,
            '  W  ' : set_wolfs_empty_cells,
            '  C  ' : set_carrot_empty_cells
        }
        func = func_handle[type.char]
        func()

        final_empties = []
        for cell in map_coordinates:
            h, w = cell
            if self.map[h][w] in cell_types:
                final_empties.append(cell)
        
        return final_empties 
        
        
    def move(self, type):
        empty_cells = self.get_empty_cells(type, is_around=True)
        if empty_cells:
            spawn_x, spawn_y = random.choice(empty_cells)
            # take the object from current cell
            self.map[type.coor[0]][type.coor[1]] = '  .  '
            if self.map[spawn_x][spawn_y] == self.food_for[type.char]: # if the chosen cell is food
                self.feed(type, spawn_x, spawn_y) # feed the object by food coordinate
            # put the object on new coordinate
            self.map[spawn_x][spawn_y] = type.char
            type.coor = (spawn_x, spawn_y)
        
        else : # if there is no empty cell it means there is no space to move and so stay 
            pass 
        
            


    def spawn(self, type):
        empty_cells = self.get_empty_cells(type) # give object as input to empty cell to determine that which are empty cells and then return them.
        spawn_x, spawn_y = random.choice(empty_cells)
        
        if self.map[spawn_x][spawn_y] == self.food_for[type.char]:
            self.feed(type, spawn_x, spawn_y)

        self.map[spawn_x][spawn_y] = type.char
        type.coor = (spawn_x, spawn_y)


    def play(self, type, types_lst):
        self.spawn(type)
        for item in types_lst:
            self.move(item)
        pass

    
                





      
game1 = GamePlay(int(sys.argv[1]), int(sys.argv[2]))


day = 0
carrot_objs = []
rabbit_objs = []
wolf_objs = []

try:
    while True:

        c = carrot('  C  ')
        carrot_objs.append(c)
        game1.spawn(c)
        # game1.play(c, carrot_objs)

        r = rabbit('  R  ')
        rabbit_objs.append(r)
        game1.play(r, rabbit_objs)

        w = wolf('  W  ')
        wolf_objs.append(w)
        game1.play(w, wolf_objs)

        day+=1
        print('day ', day)
        game1.print_day()
        time.sleep(0.1)
        os.system('clear')

except :
    print('items survived : ')
    i = 0
    for car in carrot_objs:
        print(car.char, end=' - ')
        i += 1
    for rab in rabbit_objs:
        print(rab.char, end=' - ')
        i += 1
    for wol in wolf_objs:
        print(wol.char, end=' - ')
        i += 1 
    print("\n*****************************\n" + 'there is', i-1, 'items exist now!')