#Helper Functions

#Determines what each letter in the text file should be changed to
def new_letter(key,original): 
    new_letter = (ord(original)) - (ord(key)) #Finds the new character
    while new_letter < 32: #Causes ASCII values below 32 (before space) to be wrapped around
        new_letter += 95
    return chr(new_letter)

#Uses new_letter and a keyword to decode a text_file that was encoded using vigenere 
def vigenere(text): 
    new_message = ""
    key_letter = 0 #This variable determines the current letter that is being used in the keyword to decode the character
    for t in text:
        new_message += new_letter(keyword[key_letter],t) #This adds the decoded letter to the new string
        key_letter += 1 #Progresses to the next letter in the key
        if key_letter >= len(keyword):
            key_letter = 0 #Loops back to the beginning of the keyword
    return new_message

                
#Main Code

keyword = "enigma" #The word used to decode the text file

with open("text_files/file_30d3.txt", 'r') as f:
    content = f.read()

print (vigenere(content))


