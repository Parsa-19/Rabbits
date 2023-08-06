import os
import numpy as np
import random
import time

class Rabbit:
    
    def __init__(self):
        gender_types = ["Male", "Female"]
        self.char = '  R  '
        self.coor = ()
        self.gender = random.choice(gender_types)

    


class GamePlay: 

    map = []
    temp_map = []

    def __init__(self, width = 8, height = 8):
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
                    GamePlay.map[curr_x][curr_y] = '  .  '
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
            
    


game = GamePlay()
total_rab = []
# print(GamePlay.temp_map)
while True:
    
    os.system('clear')
    game.print_map()
    
    rab = Rabbit()
    if len(GamePlay.temp_map) == 0:
        break
    game.spawn(rab)
    total_rab.append(rab)
    for obj in total_rab:
        game.move(obj)
    

    time.sleep(1)

print("Done!")




    

    
    
