class characterNode:
    def __init__(self,character,frequency):
        self.character=character
        self.frequency=frequency

    def __lt__(self, other):
        return self.frequency<other.frequency







