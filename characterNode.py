class characterNode:
    def __init__(self,character,frequency,left_node=None,right_node=None):
        self.character=character
        self.frequency=frequency
        self.left=left_node
        self.right=right_node

    def __lt__(self, other):
        return self.frequency<other.frequency







