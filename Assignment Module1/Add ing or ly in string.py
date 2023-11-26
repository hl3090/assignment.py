
word = input("Enter a word: ")
length = len(word)

if length >= 3:
     print ("Write more than 3 letters")
elif word.endswith ("ing"):
    word += "ly"
else:
    word += "ing"        
    
print (word)        
