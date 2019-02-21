#Helper Functions

#Uses a key to decode a text file
def substitute(text): 
    sub_key = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? " #The position of the characters in the key correspond to the positions of the ASCII values they replace
    new_message = ""
    for t in text:
        new_message += chr(sub_key.index(t)+32) #Finds the position of each character in the file in the key, and uses that to choose the ASCII value
    print(new_message)


#Main Code

with open("text_files/file_2715.txt", 'r') as f:
    content = f.read()

substitute(content)
