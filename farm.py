import os
import numpy as np
import random
import time
import getopt, sys

class Rabbit:
    
    def __init__(self):
        gender_types = ["Male", "Female"]
        self.char = '  R  '
        self.coor = ()
        self.gender = random.choice(gender_types)
        self.strength = 3
        self.health = 100 # 100 by default

    
    def eat_carrot(self, carrot):
        if carrot.state == True:
            print("carrot eated! wowowowo")
            self.health += 100
        else : 
            self.health -= 50
        

    def check_strength():
        pass



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
        

        if type.char == '  C  ':  # wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwaring : this may happen in same block again for carrots
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
                    # if GamePlay.map[new_x][new_y] == '  C  ':
                    #     type.eat_carrot(Carrot()) # wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwaring : there is no cordinate for the carrot that rabbit eats
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
        



    def print_map(self): 

        for i in range(len(GamePlay.map)):
            for j in range(len(GamePlay.map[i])):
                print(GamePlay.map[i][j], end = '')
            print('\n')

    

    

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
try:
    total_rab = []
    day = 0
    while True:
        
        os.system('clear')
        game.print_map()
        print(f"Day {day}:")
        day += 1
        
        
        rab = Rabbit()
        car = Carrot()
        if len(GamePlay.temp_map) == 0: # check if the game is over or not
            print("len is out of range")
            break
        game.spawn(rab)
        game.spawn(car)
        total_rab.append(rab)
        for obj in total_rab:
            game.move(obj)
        
        print(len(GamePlay.temp_map))
        time.sleep(day_late)
        
        
    print("Done!")
except:
    print(f"this is the exception: \nlen(temp)is:{len(GamePlay.temp_map)}")
    for i in range(len(GamePlay.temp_map)):
            print(GamePlay.temp_map[i])




    

    
    
