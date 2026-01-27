class Volume:
    def __init__(self, vol=0):
        self.set(vol)

    def __repr__(self):
        return f"Volume({self._vol})"

    def set(self, vol):
        if vol < 0:
            self._vol = 0
        elif vol > 11:
            self._vol = 11
        else:
            self._vol = vol

    def get(self):
        return self._vol

    def up(self, amount):
        self.set(self._vol + amount)

    def down(self, amount):
        self.set(self._vol - amount)

    def __eq__(self, other):
        if isinstance(other, Volume):
            return self._vol == other._vol
        return False


def partyVolume(filename):
    with open(filename, "r") as f:
    
        initial_volume = float(f.readline())
        vol = Volume(initial_volume)

        for line in f.readlines():
            command, amount = line.split()
            amount = float(amount)

            if command == 'U':
                vol.up(amount)
            elif command == 'D':
                vol.down(amount)

    return vol

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py'))
