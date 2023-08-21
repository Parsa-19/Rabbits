import os
import random
import time
import getopt, sys

class Creature:
    def __init__(self, char, age='adult'):
        self.char = char
        self.coor = ()
        self.gender = random.choice(["Male", "Female"])
        self.health = 100 # 100 by default
        self.stomach = 0
        self.age = age






class Wolf(Creature):  
    def __init__(self, char, age='adult'):
        super().__init__(char, age)


class Rabbit(Creature):
    def __init__(self, char, age='adult'):
        super().__init__(char, age)


class Carrot:
    def __init__(self):
        self.char = '  C  '
        self.coor = ()
        self.state = random.choice([True, True, True, True, False])


class GamePlay: 

    map = []
    temp_map = []

    total_wols = [] # keep objects
    total_rabs = []
    total_cars = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        for x in range(self.height):
            line_append = []
            for y in range(self.width):
                line_append.append('  .  ')
                GamePlay.temp_map.append((x, y))
            GamePlay.map.append(line_append)
    

    def spawn(self, type, put_coor):
        
        x, y = put_coor
         
        GamePlay.map[x][y] = type.char
        type.coor = put_coor
        

        if type.char == '  C  ':  
            pass
        elif GamePlay.temp_map:
            GamePlay.temp_map.remove(put_coor)
    
    
    def get_around(self, type):
        curr_x, curr_y = type.coor # current x and current y
        around = [(curr_x, curr_y-1), (curr_x, curr_y+1),
                  (curr_x-1, curr_y), (curr_x+1, curr_y)]
        return around


    def move(self, type):
        possible_moves = self.get_around(type)
        
        while possible_moves: 
            destin_x, destin_y = random.choice(possible_moves)

            if (destin_x, destin_y) in GamePlay.temp_map:
                    
                    if GamePlay.map[destin_x][destin_y] == '  C  ':
                        carrot_x, carrot_y = destin_x, destin_y
                        self.feed(type, (carrot_x, carrot_y), GamePlay.total_cars)
                    


                    GamePlay.map[type.coor[0]][type.coor[1]] = '  .  ' # remove the rab from current possition
                    GamePlay.temp_map.append(type.coor) # take back the current location that rabbit was taken
                    type.coor = (destin_x, destin_y) # set the new location 
                    GamePlay.temp_map.remove((destin_x, destin_y)) # remove the new location from temprory
                    GamePlay.map[destin_x][destin_y] = type.char
                    break
            else:
                possible_moves.remove((destin_x, destin_y))


        
    
    def check_partner(self, type):
        around_cells = self.get_around(type)

        for x, y in around_cells:
            if x >= 0 and x < len(GamePlay.map[0]) and y >= 0 and y < len(GamePlay.map): # if the cell's coordinate was in map;

                for rab_ins in GamePlay.total_rabs:
                    if rab_ins.coor == (x, y):
                        if rab_ins.gender == "Female" and rab_ins.age == 'adult':
                            return True  
        return False
    
    
    def generate_rab(self, type):
        around_cells = self.get_around(type)
        while around_cells:
            x, y = random.choice(around_cells)
            if (x, y) in GamePlay.temp_map:
                rab = Rabbit('  r  ', 'baby')
                self.spawn(rab, (x, y))
                return rab
            else:
                around_cells.remove((x, y))
            
        return None # return none when there is no place to generate new rab


    def health_check(self, type):
        if type.health <= 0: 
            return False
        return True


    def feed(self, type, food_coor, total_food_obj):  # [0]:the item that you wanna feed | [1]:food coordinate | [2]:whole the food objects  
        type.stomach += 1
        # search between all food instances (carrots or rabbits it could be) to see wich food instance is found by eater and then feed it
        for food in total_food_obj:
            if food.coor == food_coor:
                total_food_obj.remove(food)

                if food.char == '  R  ':
                    type.health += 100
                elif food.char == '  C  ':
                    if food.state == True:
                        type.health += 100
                    else:
                        type.health -= 50



    def print_map(self): 
        for i in range(len(GamePlay.map)):
            for j in range(len(GamePlay.map[i])):
                print(GamePlay.map[i][j], end = '')
            print('\n')
                

    def get_rabbit_info(self):
        for rab_ins in GamePlay.total_rabs:
            print(f'{rab_ins.char} --> {rab_ins.health}  |  carrot eaten: {rab_ins.stomach}  |  gender:{rab_ins.gender}')
        for wol_ins in GamePlay.total_wols:
            print(f'{wol_ins.char} --> {wol_ins.health}  |  carrot eaten: {wol_ins.stomach}  |  gender:{wol_ins.gender}')

    def add_rab(self, type):
        GamePlay.total_rabs.append(type)

    def kill_rab(self, type):
        GamePlay.total_rabs.remove(type)
        del type
    



###################### main ######################
if __name__ == '__main__':

    day_late = 1 # second
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'w:h:t:')
    W, H = 9, 9
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

# try :
    while GamePlay.temp_map:
        os.system('clear')
        print(f"Day {day}:")


        car = Carrot()
        GamePlay.total_cars.append(car)
        game.spawn(car, random.choice(GamePlay.temp_map) if GamePlay.temp_map else (0, 0))

        rab = Rabbit('  R  ')
        GamePlay.total_rabs.append(rab)
        game.spawn(rab, random.choice(GamePlay.temp_map) if GamePlay.temp_map else (0, 0)) # spawn gets object and a tuple for set the object's cordinate in map

        # wol = Wolf('  W  ')
        # GamePlay.total_wols.append(wol)
        # game.spawn(wol, random.choice(GamePlay.temp_map) if GamePlay.temp_map else (0, 0)


        for rab in GamePlay.total_rabs:
            game.move(rab)
            if rab.age == 'adult' and rab.gender == 'Male':
                in_love = game.check_partner(rab)
                if in_love == True:
                    cuple_found += 1
                    new_rab = game.generate_rab(rab) # gener_rab method need the father's rab obj
                    if new_rab: # if new_rab is containing a rab object in it, now it can take place in total_rabs
                        game.add_rab(new_rab)
                        baby_generated += 1

            rab_stat = game.health_check(rab)
            if rab_stat == False:
                game.kill_rab(rab)
        
        for wol in GamePlay.total_wols:
            game.move(wol)
                

        
        game.print_map()
        time.sleep(day_late)
        day += 1

    print("Done!")
    print(f'\n -{died_rabs}- nafar fot shodan')
    print(f' -{cuple_found}- times rabbits have gotten married')
    print(f' -{baby_generated}- babies borned')
    game.get_rabbit_info()
        
# except KeyboardInterrupt :
#     print(f'\n -{died_rabs}- nafar fot shodan')
#     print(f' -{cuple_found}- times rabbits have gotten married')
#     print(f' -{baby_generated}- babies borned')
#     game.get_rabbit_info()
    
        
###################### main ######################

