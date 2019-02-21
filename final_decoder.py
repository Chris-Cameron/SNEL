import message_finder #This decoder borrows functions from message finder to loop through the text files

message = ""

num_files = 18000 #The number of files to be looped through
for n in range(num_files): 
    file_name = message_finder.get_file_name(n) #Uses a function from the message finder to convert the numbers into hexadecimal-based file names
    text = message_finder.get_file_content("text_files/" + file_name) #Uses a function from the message finder to retreive the file content
    message += text[0] #Adds the first letter of each text file to the final message

print(message)
    
