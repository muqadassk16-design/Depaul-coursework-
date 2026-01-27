#problem 1

class Pizza:
    """
    A class representing a pizza with size and toppings.

    """
    _base_prices = {'S': 6.25, 'M': 9.95, 'L': 12.95}
    _topping_prices = {'S': 0.70, 'M': 1.45, 'L': 1.85}

    def __init__(self, size='M', toppings=None):
        self.size = size
        self.toppings = set() if toppings is None else set(toppings)

    def setSize(self, size):
        if size in ('S', 'M', 'L'):
            self.size = size
        else:
            raise ValueError("Size must be 'S', 'M', or 'L'.")

    def getSize(self):
        return self.size

    def addTopping(self, topping):
        self.toppings.add(topping)

    def removeTopping(self, topping):
        self.toppings.discard(topping)

    def price(self):
        return self._base_prices[self.size] + self._topping_prices[self.size] *len(self.toppings)
    def __repr__(self):
        toppings_sorted = sorted(self.toppings)
        return "Pizza('{}', {{{}}})".format(
        self.size,
        ', '.join(f"'{t}'" for t in toppings_sorted)
    )
    def __eq__(self, other):
        return isinstance(other, Pizza) and self.size == other.size and self.toppings == other.toppings
 


def orderPizza():
    """
    Allows the user to interactively build a pizza and returns it.
    """
    print("Welcome to Python Pizza!")
    

    while True:
        size = input("What size pizza would you like (S,M,L): ").upper()
        if size in ('S', 'M', 'L'):
            break
        print("Invalid size. Please enter S, M, or L.")
    
    pizza = Pizza(size)
    

    while True:
        topping = input("Type topping to add (or Enter to quit): ").strip()
        if topping == '':
            break
        pizza.addTopping(topping)
    
    print("Thanks for ordering!")
    print(f"Your pizza costs ${pizza.price()}")
    print(pizza)
    
    return pizza





if __name__ == '__main__':
    import doctest
    print( doctest.testfile( 'hw2TEST.py'))
