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

    def eat_carrot(self, carrot_x, carrot_y): 
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

    def __init__(self, width = 6, height = 6):
        self.width = width
        self.height = height
        
        for x in range(self.width):
            line_append = []
            for y in range(self.height):
                line_append.append('  .  ')
                GamePlay.temp_map.append((x, y))
            GamePlay.map.append(line_append)
    

    @staticmethod
    def spawn(type):
        rand_coor = random.choice(GamePlay.temp_map)
        x, y = rand_coor
        
        GamePlay.map[x][y] = type.char
        type.coor = rand_coor
        

        if type.char == '  C  ':  
            pass
        else:
            GamePlay.temp_map.remove(rand_coor)
    

    @staticmethod
    def move(type):
        curr_x, curr_y = type.coor # current x and current y
        possible_moves = [(curr_x, curr_y-1), (curr_x, curr_y+1),
                        (curr_x-1, curr_y), (curr_x+1, curr_y)]
        
        while True: # do it 'till it breaks
            if possible_moves: 
                choosen_block = random.choice(possible_moves)
                new_x, new_y = choosen_block
                if (new_x, new_y) in GamePlay.temp_map:
                    if GamePlay.map[new_x][new_y] == '  C  ':
                        type.eat_carrot(new_x, new_y)
                        type.strength = 3
                    GamePlay.map[curr_x][curr_y] = '  .  ' # remove the rab from current possition
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
        



    def print_map(self): 
        for i in range(len(GamePlay.map)):
            for j in range(len(GamePlay.map[i])):
                print(GamePlay.map[i][j], end = '')
            print('\n')


    @staticmethod
    def get_health():
        for rab_ins in gc.get_objects():
            if isinstance(rab_ins, Rabbit):
                print(rab_ins.char, '-->', rab_ins.health)

    



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

    total_rabs = []
    day = 0

    died_rabs = 0
    try :
        while True:
            
            os.system('clear')
            print(f"Day {day}:")
            day += 1    
            
            rab = Rabbit()
            car = Carrot()
            game.spawn(rab)
            # the last rab in last day will fill the last cell so temp_map now has nothing in it and when it spawn carrot there is nothing to choose between. so i created a if to check temp_map and finish the game (SO SPAWN CARROT WONT BE RUN THIS TIME) 
            if len(GamePlay.temp_map) == 0: # check if the game is over or not
                game.print_map()
                time.sleep(day_late)
                break
            game.spawn(car)

            total_rabs.append(rab)
            for obj in total_rabs:
                obj.strength -= 1
                game.move(obj)
                rab_stat = game.check_rab_strength(obj)
                if rab_stat == False:
                    total_rabs.remove(obj)
                    died_rabs += 1 

            
            game.print_map()
            time.sleep(day_late)

        print("Done!")
        
    except :
        print(died_rabs, "nafar fot shodan")
        
        
###################### main ######################