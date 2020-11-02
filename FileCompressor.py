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





