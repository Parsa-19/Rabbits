import time 


# create list of dots with positions 
def create_dot_list(width, height):
    dot = []
    for h in range(height):
        dot_line = []
        for w in range(width):
            dot_line.append('   .   ')
        dot.append(dot_line)

    print("the list is successfully created!")
    return dot
'''
>>> input : 3
>>> input : 3
dot = [ ['x1', 'x2', 'x3'], ['x1', 'x2', 'x3'], ['x1', 'x2', 'x3'] ]
                             ---
>>> dot[1][0]
>>> output : x2
x2 in list 2
'''




# print map in the terminal
def print_map(dot):
    
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n')


height = int(input("height : "))
width = int(input("width : "))

dot = create_dot_list(width, height)

# counts days and provides map
num_of_days = 0 
while True:
    num_of_days += 1
    print(f"day{num_of_days}")

    print_map(dot)
    time.sleep(1)