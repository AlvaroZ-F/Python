"""
    Create an script that'd receive a text document and do the following:
        - Show the repeated words, and create a dictionary with these as keys, and how many times they've repeated.
        - Consider any signs of punctuation (commas, periods, spaces...)
        - Count how many words there are in the document.
"""

def wordRepCount(doc):
    countDict = {}
    text = doc.read().split()

    for word in text:
        if word not in countDict.keys():
            countDict[word] = 1
        else:
            countDict[word] += 1
    return countDict

def wordCount(doc):
    count = 0
    text = doc.read().split()

    for word in text:
        count += 1

    return count
            
docu = open("document.txt","r")
print( wordRepCount(docu) )
print("Word count: ")
print(wordCount(docu))
