# class test_class:
#     def __init__(self, name):
#         self.name = name
#         self.put()


#     def put(self):
#         print(f"put {self.name} done! placed")

#     def move(self):
#         print(f"    obj {self.name} is moved! thank you!")


# tes = []
# i = 0
# while i < 4:
#     tes.append(test_class(f"this_{i}"))


#     for rab in tes:
#         rab.move()

#     i += 1
import time
import random

my_dict = {
    '0':[0, 1, 2, 3, 4, 5],
    '1':[0, 1, 2, 3, 4, 5],
    '2':[0, 1, 2, 3, 4, 5],
    '3':[0, 1, 2, 3, 4, 5],
    '4':[0, 1, 2, 3, 4, 5],
    '5':[0, 1, 2, 3, 4, 5],
    '6':[]
}

def print_dict(dic):
    for i in dic:
        for j in dic[i]:
            print(j, end='      ')
        print('\n')
        


keys = []
for i in my_dict:
    keys.append(i)

print(len(my_dict))
i = 0
while i <= 6:
    i += 1

    

    # line = random.choice(keys)
    # item = random.choice(my_dict[line])
    
    # print(f"selected line {line}")
    # print(f"selected item {item}")
    # my_dict[line].remove(item)

    # print_dict(my_dict)
    

    # time.sleep(2)
    if len(my_dict['6']) == 0:
        my_dict.pop('6')
        print("deleted")
        break
print(len(my_dict))
