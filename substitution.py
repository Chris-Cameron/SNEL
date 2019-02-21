#Helper Functions

#"Inverts" the ASCII values of the characters in the text file, so that those at the beginning go towards the end and vice-versa
def substitute(text): 
    new_message = ""
    for t in text:
        new_message += chr(158-ord(t)) #158 is 32+126, which is why it is used for the inversion
    print(new_message)


#Main Code

with open("text_files/file_2715.txt", 'r') as f:
    content = f.read()

substitute(content)
    
        
