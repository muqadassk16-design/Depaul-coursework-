class Counter(dict):
    def count(self, item):
        # Increment the count for a single item
        self[item] = self[item] + 1

    def countItems(self, items):
        # Count all items in an iterable
        for item in items:
            self.count(item)

    def __getitem__(self, key):
        # Return 0 if the key has not been counted
        return dict.get(self, key, 0)

    def __repr__(self):
        # Display as Counter({key: count, ...})
        return f"Counter({dict.__repr__(self)})"

    def printCounts(self):
        # Print keys in sorted order
        for key in sorted(self):
            print(key, self[key])


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab4TEST.py'))
