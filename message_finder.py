#Helper Functions

#Find the chi-squared value from a list of numbers
def chi_squared(counts): #each value in counts is the number of a specific ASCII character
    chi = 0
    expected = sum(counts)/len(counts) #The expected amount of each character
    for c in counts:
        chi += ((c-expected)**2)/(expected)
    return chi

#Finds the amount of each character in a string
def get_char_counts(text): 
    counts = [0]*95 #Creates an empty array
    for i in range (32, 127): #This range is used to check for each ASCII character that will be used in the messages
        counts[i-32] = text.count(chr(i))
    return counts

def get_file_name(num): #Gets the file name corresponding to a decimal number
    if num == 0:
        return "file_0000.txt" #This deals with an exception to the solution for adding leading zeroes below, where the use of "0" would cause leading zeroes to be added infinitely
    name= "file_"
    old_num = format(num,'x') #This converts integers into hexadecimal without the "0x" resulting from hex()
    while num < 4096: #4096 and 16 are used to account for the amount characters that would be in a hexadecimal number
        name += "0" #Adds a leading zero
        num *= 16
    name += str(old_num) + ".txt"
    return name
    
def get_file_content(file_name):#Converts content of a text file into a string
    with open(file_name, 'r') as f: 
        content = f.read()
    return content


#Main Code

if __name__ == "__main__":
    
    num_files = 18000 #Amount of files to be looped through
    threshold = 150 #Minimum Chi-Square Value to Be Printed

    for n in range(num_files):
        file_name = get_file_name(n) 
        text = get_file_content("text_files/" + file_name) 
        counts = get_char_counts(text)
        chi_square = chi_squared(counts)

        if chi_square > threshold: #Prints suspicious files
            print(file_name, chi_square) 
        
