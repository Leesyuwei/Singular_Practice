class Bottle():
    def __init__(self):
        self.quantity=0

    def add_water(self,quantity):
        self.quantity+=quantity

bottle=Bottle()

while 1:
    print(bottle.quantity)
    bottle.add_water(int(input()))