def main():
    
    # opens the file with the letter matrix
    wordFile = open('/Users/hgoscenski/Desktop/puzzle.txt', 'r')
    
    # Initializes lists to store letter matrix in
    rowList = []
    columnList = []
    
    # Iterates through file input to create rowList and columnList
    for line in wordFile:
        rowList.append(line.split())
    
    # used to ensure the flip is within the index to prevent errors
    length = len(rowList[0])
    
    # flips the rowList to create the columnList
    for i in range(length):
        columnList.append([row[i] for row in rowList])

    # opens the file with the words to be found
    tofind = open('/Users/hgoscenski/Desktop/wordList.txt', 'r')
    words = []
    for line in tofind:
        words.append(line.split())
        
    #  REMEMBER TO CHANGE S TO WHAT IT IS SUPPOSED TO BE
    valueDict = {'a': 5, 'b': 7, 'c': 8, 'd': 1, 'e': 7, 'f': 12, 
                 'g': 1, 'h': 4, 'i': 12, 'j': 8, 'k': 6, 'l': 3, 
                 'm': 5, 'n': 1, 'o': 3, 'p': 2, 'q': 8, 'r': 10, 
                 's': 0, 't': 12, 'u': 3, 'v': 7, 'w': 1, 'x': 3, 
                 'y': 2, 'z': 1}
    rowValueDict = {0:8, 1:2, 2:5, 3:3, 4:7, 5:9, 6:2}

    # Initiializes lists to store words that are found and not found
    found = []
    foundDict = {}
    notFound = []
    newWords = []
    
    def score(word):
        total = 0
        for x in word:
            total += valueDict[x]
        return(total)
        
    # Creates function findFunc- with inputs of both horizontal and vertical rows, and words to search for
    def findFunc(listType1, listType2, wordToFind):
        # Iterates though rows for searching for wordToFind
        wordValue = 0
        for a,b in enumerate(listType1):
            b = ''.join(b)
            if wordToFind in b:
                found.append(wordToFind)
                wordValue = score(wordToFind) + rowValueDict[a] 
                foundDict[wordValue] = wordToFind
                print('Row: ' + str(a + 1) + ' (' + wordToFind + ') -Found! Score:', wordValue)
                
        # Iterates through rows backwards 
        for a,b in enumerate(listType1):
            b = ''.join(b)
            b = b[::-1]
            if wordToFind in b:
                found.append(wordToFind)
                found.append(wordToFind)
                wordValue = score(wordToFind) + rowValueDict[a] 
                foundDict[wordValue] = wordToFind
                print('Backwards Row: ' + str(a + 1) + ' (' + wordToFind + ') -Found! Score:', wordValue)
 
        # Iterates though columns for searching for wordToFind         
        for a,b in enumerate(listType2):
            b = ''.join(b)
            if wordToFind in b:
                found.append(wordToFind)
                wordValue = score(wordToFind)
                foundDict[wordValue] = wordToFind
                print('Column: ' + str(a + 1) + ' (' + wordToFind + ') -Found! Score:', wordValue)
                
        # Iterates through columns backwards   
        for a,b in enumerate(listType2):
            b = ''.join(b)
            b = b[::-1]
            if wordToFind in b:
                found.append(wordToFind)
                wordValue = score(wordToFind)
                foundDict[wordValue] = wordToFind
                print('Backwards Column: ' + str(a + 1) + ' (' + wordToFind + ') -Found! Score:', wordValue)
    
    # Iterating through the words nested list
    for i,x in enumerate(words):
        x = x[0]
        
        # Takes the words 'list in list' and turns it into a regular list
        newWords.append(x)
        
        # function call to actually perform search for all words 
        findFunc(rowList, columnList, x)

  
    # Sorts through newWords (list of words to find) and removes any words that were found
    for x in newWords:
        if x not in found:
            # adds words not found to notFound list
            notFound.append(x)
    
    # for x in found:
    #     print(x, ' is worth:', score(x))
        
        
    # Prints both the found and not found words
    print()
    print('These words were found:')
    for key in sorted(foundDict, reverse=True):
        print (foundDict[key], 'is equal to:', key)
    print()
    print('These words were not found:', notFound)
   
main()
