from heapq import heapify
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


def main():
    frequencyTable=generateFrequencyTable("WarAndPeace.txt")
    createHeap(frequencyTable)






