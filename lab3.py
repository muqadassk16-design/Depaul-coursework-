class Stack:
    def __init__(self, items=None):
        '''create an empty stack.The first item is the bottom, the last is the
           top.'''
        
        if items is None:
            self._data = []
        else:
            self._data = list(items)

    def push(self, item):
       '''Push an item onto the top of the stack.'''
       self._data.append(item)

    def pop(self):
        '''Remove and return the item at the top of the stack.'''
        return self._data.pop()

    def isEmpty(self):
        '''Return True if the stack is empty, False if not'''
        return len(self._data) == 0

    def __len__(self):
        '''Return the number of items in the stack.'''
        return len(self._data)

    def __getitem__(self, index):
        '''Return the item at the given index (0 is bottom of stack).'''
        return self._data[index]

    def __repr__(self):
        '''Return a string representation of the stack.'''
        return f"Stack({self._data})"

if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab3TEST.py') )
