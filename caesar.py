#Helper Functions

#Finds the most common character in the text file
def most_common(text):
    counts = [0]*95 #Creates an array to store the amount of each character present
    for i in range (32, 127):
        counts[i-32] = text.count(chr(i)) #Selects a specific character and stores the amount
    return counts.index(max(counts))+32

#Shifts all of the ASCII values in the text so that the most common character is mapped to space
def caesar(text):
    new_message = "" 
    shift = 127-most_common(text) #Calculates how much the value of the shift must be; 127 is used because it wraps around to 32, or space.
    for t in text:
        new_value = ord(t) + shift #Shifts each character
        if new_value > 126: #Causes values above 126 to wrap around to the beginning of the valid ASCII characters
            new_value-= 95 
        new_message += chr(new_value) #Adds the shifted character to a new string
    print(new_message) 


#Main Code
    
with open("text_files/file_063d.txt", 'r') as f:
    content = f.read()

caesar(content)


