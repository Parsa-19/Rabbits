import os # clear
import sys, getopt # take parametr





class Rabbits:
    pass

class Carrot:
    pass

class Farm:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def create_map(self):
        




def get_parametrs(argv):
    opts, args = getopt.getopt(argv, 'w:h:')
    width, height = 0
    for op, ar in opts:
        if op == '-w':
            width = int(ar)
        elif op == '-h':
            height = int(ar)

    if width and height:
        return width, height





if __name__ == "__main__":


    width, height = get_parametrs(sys.argv[1:])
    farm = Farm()
    try:
        while True:
            pass
        
    except:
        pass