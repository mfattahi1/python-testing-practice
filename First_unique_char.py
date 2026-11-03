def first_unique_char(text):
    
    ourDict={}
    for char in text:
        ourDict[char] = ourDict.get(char,0) + 1
    
    for key,value in ourDict.items():
        if value ==1:
            return key


