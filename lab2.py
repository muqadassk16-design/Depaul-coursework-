class BagOfDonuts:
    def __init__(self, number=12, style='cake', addons='none'):
        self.number = number
        self.style = style
        self.addons = addons

    def __repr__(self):
        return f"BagOfDonuts({self.number}, '{self.style}', '{self.addons}')"

    def setNumber(self, number):
        self.number = number

    def setStyle(self, style):
        self.style = style

    def setAddons(self, addons):
        self.addons = addons

    def price(self):
        return round(self.number * 0.99, 2)

    def printOrder(self):
        print(
            f"A bag of {self.number} {self.style} donuts "
            f"covered with {self.addons} costs ${self.price():.2f}."
        )


def getOrders(filename):
    orders = []

    with open(filename, 'r') as file:
        for line in file:
            number, style, addons = line.strip().split(',')
            bag = BagOfDonuts(int(number), style, addons)
            bag.printOrder()
            orders.append(bag)

    return orders

if __name__=='__main__':

import doctest
print( doctest.testfile('lab2TEST.py') )


        
