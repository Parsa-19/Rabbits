import os
import random
import time
import getopt, sys
import gc

class Rabbit:
    def __init__(self):
        gender_types = ["Male", "Female"]
        self.char = '  R  '
        self.coor = ()
        self.gender = random.choice(gender_types)
        self.strength = 4 # first time it spawns and moves at same time (when it moves, it decrease) so I put 4
        self.health = 100 # 100 by default
        self.stomach = 0

    def eat_carrot(self, carrot_x, carrot_y): 
        self.stomach += 1
        # search between all carrot instances to see wich carrot is found by rabbit and then feed it
        for carrot in gc.get_objects():
            if isinstance(carrot, Carrot):
                if carrot.coor == (carrot_x, carrot_y):
                    
                    if carrot.state == True:
                        self.health += 100
                    else :
                        self.health -= 50





class Carrot:
    def __init__(self):
        self.char = '  C  '
        self.coor = ()
        self.state = random.choice([True, True, True, True, False])
    


class GamePlay: 

    map = []
    temp_map = []
    total_rabs = []

    def __init__(self, width = 6, height = 6):
        self.width = width
        self.height = height
        
        for x in range(self.height):
            line_append = []
            for y in range(self.width):
                line_append.append('  .  ')
                GamePlay.temp_map.append((x, y))
            GamePlay.map.append(line_append)
    

    @staticmethod
    def spawn(type, put_coor):
        
        x, y = put_coor
         
        GamePlay.map[x][y] = type.char
        type.coor = put_coor
        

        if type.char == '  C  ':  
            pass
        else:
            if GamePlay.temp_map:
                GamePlay.temp_map.remove(put_coor)
    
    
    @staticmethod
    def get_around(type):
        curr_x, curr_y = type.coor # current x and current y
        around = [(curr_x, curr_y-1), (curr_x, curr_y+1),
                        (curr_x-1, curr_y), (curr_x+1, curr_y)]
        return around


    def move(self, type):
        possible_moves = self.get_around(type)
        
        while True: # do it 'till it breaks
            if possible_moves: 
                choosen_block = random.choice(possible_moves)
                new_x, new_y = choosen_block
                if (new_x, new_y) in GamePlay.temp_map:

                    if GamePlay.map[new_x][new_y] == '  C  ':
                        type.eat_carrot(new_x, new_y)
                        type.strength = 3
                    elif GamePlay.map[new_x][new_y] == '  .  ':
                        type.strength -= 1

                    GamePlay.map[type.coor[0]][type.coor[1]] = '  .  ' # remove the rab from current possition
                    GamePlay.temp_map.append(type.coor) #take back the current location that rabbit was taken
                    type.coor = (new_x, new_y) # set the new location 
                    GamePlay.temp_map.remove(choosen_block) # remove the new location from temprory
                    GamePlay.map[new_x][new_y] = type.char
                    break
                else:
                    possible_moves.remove(choosen_block)
            else:
                break

    
    @staticmethod
    def check_rab_strength(type):
        if type.strength == 0:
            x, y = type.coor
            GamePlay.map[x][y] = '  .  ' 
            GamePlay.temp_map.append(type.coor)
            return False
        else:
            # you'll be still alive
            return True
        
    
    def check_partner(self, type):
        around_cells = self.get_around(type)

        for x, y in around_cells:
            if x >= 0 and x < len(GamePlay.map[0]) and y >= 0 and y < len(GamePlay.map): # if the cell's coordinate was in map;

                for rab_ins in gc.get_objects():
                    if isinstance(rab_ins, Rabbit):
                        if rab_ins.coor == (x, y):
                            if rab_ins.gender == "Female":
                                return True  
        return False
    

    def generate_rab(self, type):
        around_cells = self.get_around(type)
        while True:
            if around_cells:
                x, y = random.choice(around_cells)
                if (x, y) in GamePlay.temp_map:
                    rab = Rabbit()
                    self.spawn(rab, (x, y))
                    return rab
                else:
                    around_cells.remove((x, y))
            else:
                break 
        return None # return none when there is no place to generate new rab
            
        

    @staticmethod
    def print_map(): 
        for i in range(len(GamePlay.map)):
            for j in range(len(GamePlay.map[i])):
                print(GamePlay.map[i][j], end = '')
            print('\n')


    @staticmethod
    def get_rabbit_info():
        for rab_ins in gc.get_objects():
            if isinstance(rab_ins, Rabbit):
                print(rab_ins.char, '-->', rab_ins.health, ' | carrots eaten: ', rab_ins.stomach)

    @staticmethod
    def add_rab(type):
        GamePlay.total_rabs.append(type)

    @staticmethod
    def kill_rab(type):
        GamePlay.total_rabs.remove(type)
        del type
    



###################### main ######################
if __name__ == '__main__':

    day_late = 1 # second
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'w:h:t:')
    W, H = 6, 6
    for op, ar in opts:
        if op == '-w':
            W = int(ar)
        elif op == '-h':
            H = int(ar)
        elif op == '-t':
            day_late = float(ar)

    game = GamePlay(W, H) # width, height

    
    day = 0

    died_rabs = 0
    cuple_found = 0
    baby_generated = 0 
try :
    while True:
        os.system('clear')
        print(f"Day {day}:")
        day += 1
        
        rab = Rabbit()
        game.spawn(rab,random.choice(GamePlay.temp_map) if GamePlay.temp_map else (0, 0)) # spawn gets object and a tuple for cordinate the object in map
        # the last rab in last day will fill the last cell so temp_map now has nothing in it and when it spawn carrot there is nothing to choose between. so i created a if to check temp_map and finish the game (SO SPAWN CARROT WONT BE RUN THIS TIME) 
        if len(GamePlay.temp_map) == 0: # check if the game is over or not
            game.print_map()
            time.sleep(day_late)
            break
        car = Carrot()
        game.spawn(car, random.choice(GamePlay.temp_map) if GamePlay.temp_map else (0, 0))


        GamePlay.total_rabs.append(rab)
        for obj in GamePlay.total_rabs:
            game.move(obj)

            in_love = game.check_partner(obj)
            if in_love == True:
                cuple_found += 1
                new_rab = game.generate_rab(obj) # gener_rab method need the father's rab obj
                if new_rab: # if new_rab is containing a rab in it, now it can take place in total_rabs
                    game.add_rab(new_rab)
                    baby_generated += 1

            rab_stat = game.check_rab_strength(obj)
            if rab_stat == False:
                
                game.kill_rab(obj)
                died_rabs += 1

        
        game.print_map()
        time.sleep(day_late)

    print("Done!")
        
except :
    print(f'\n -{died_rabs}- nafar fot shodan')
    print(f' -{cuple_found}- times rabbits have gotten married')
    print(f' -{baby_generated}- babies borned')
    game.get_rabbit_info()
    
        
###################### main ######################

