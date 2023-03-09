# Chapter 4 - Cracking Codes With Python - Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

# Reverse Cipher



message = input('Enter Message: ')   # user enters message they want to reverse cipher  
translated = ''      # This variable is where the program is storing the translated string


i = len(message) - 1         # Variable i storing value from len function. Len() uses variable message to return an integrer value for how many characters are in message. It has to subtract 1 due to index.
while i >= 0:             # While loop WHILE 'CONDITION" ":" Then indented block of code running in the loop as long as the condition is true. boolean data is True or False, not string
    translated = translated + message[i]            #stores current value in translated based on index i in message, string grows one character per loop, until message string translated
 #   print('i is', i, ', message[i] is', message[i], ', translated is', translated)       #line to demonstrate how the loop works. Can comment out for normal program. 
    i = i - 1   #decrementing the variable

print(translated) #prints the reverse of the original message after the string is processed through the while loop    


# i = length of message - 1 for index. Translate stores the indexed concatenated sting one character at a time because each loop is decrementing variable i by 1, eventually i = -1 and the loop exits 
# index is the integer value of each character in the string. By selecting i = len -1 that tells python to display the total number of characters in message. 
#The variable translated is storing messages + the index, but it is not storing the integer value from length, but the string value from message based on the characters index number. 
#This allows translate to character by character build a string in translate variable that is the exact reverse of the string in message variable.  




