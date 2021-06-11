import random

class Actor:
    def __init__(self):
        self.position1 = random.randint(10,50)
        self.position2 = random.randint(10,50)
        self.position3 = random.randint(10,50)
        self.position4 = random.randint(10,50)
        self.position5 = random.randint(10,50)

        self.position1y = random.randint(1,4)
        self.position2y = random.randint(5,8)
        self.position3y = random.randint(9,12)
        self.position4y = random.randint(13,16)
        self.position5y = random.randint(17,19)

    def move_letters(self):
        if self.position1 == 60:
            self.position1 = 0
        else:
            self.position1 += 1
        if self.position2 == 60:
            self.position2 = 0
        else:
            self.position2 += 1
        if self.position3 == 60:
            self.position3 = 0
        else:
            self.position3 += 1
        if self.position4 == 60:
            self.position4 = 0
        else:
            self.position4 += 1
        if self.position5 == 60:
            self.position5 = 0
        else:
            self.position5 += 1


