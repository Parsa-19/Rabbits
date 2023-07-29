class test_class:
    def __init__(self, name):
        self.name = name
        self.put()


    def put(self):
        print(f"put {self.name} done! placed")

    def move(self):
        print(f"    obj {self.name} is moved! thank you!")


tes = []
i = 0
while i < 4:
    tes.append(test_class(f"this_{i}"))


    for rab in tes:
        rab.move()

    i += 1