
# Write a program in Python using Regular Expressions which will print the count of all alphabetic characters in a given text 

import re

while True:
    text = input("Enter the text: ")
    if len(text) > 0:
        break

def letterCount(text):
    pattern = "\w"
    countOfLetter = re.findall(pattern, text)
    return len(countOfLetter)

print(letterCount(text))