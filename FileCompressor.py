from heapq import heapify,heappop
from HuffmanEncoding.characterNode import characterNode

#create a hashmap with characters as keys and frequencies as values
def generateFrequencyTable(file_name):

    frequencyTable={}

    file=open(file_name,"r")

    for line in file:
        for character in line:
            if character in frequencyTable:
                frequencyTable[character]=frequencyTable[character]+1

            else:
                frequencyTable[character]=1

    file.close()

    return frequencyTable


#Add nodes to priority queue
def createHeap(frequencyTable):
    heap=[]
    for character in frequencyTable:
        node=characterNode(character,frequencyTable[character])
        heap.append(node)
    heapify(heap)

    return heap


# Create Tree
def createTree(heap):
    while len(heap) > 1:
        right_node = heappop(heap)
        left_node = heappop(heap)
        new_node = characterNode(character=None, frequency=right_node.frequency + left_node.frequency,
                                 left_node=left_node, right_node=right_node)
        heap.append(new_node)


def main():
    frequencyTable=generateFrequencyTable("WarAndPeace.txt")
    heap=createHeap(frequencyTable)
    createTree(heap)








