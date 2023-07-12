import time

def create_dot_list(width, height):
    dot = []
    for h in range(height):
        dot_line = []
        for w in range(width):
            dot_line.append('   .   ')
        dot.append(dot_line)

    return dot

def print_field(dot):
    
    for h in range(len(dot)):
        for w in dot[h]:
            print(w, end='')
        print('\n')



height = int(input("height : "))
width = int(input("width : "))

dot = create_dot_list(width, height)

num_of_days = 0 
while num_of_days < 10:
    num_of_days += 1

    print(f"index = {num_of_days}")
    #2:
    print_field(dot)
    time.sleep(1)
