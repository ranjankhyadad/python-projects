import json
import difflib # to predict similar words 
from difflib import get_close_matches

# Can't open the file using filehandling method because the read method gives 
# data as a string or string of bytes and not as a dict

#  with open("data.json") as mydatasource:
#     mydata= mydatasource.read()
#     print(mydata)

mydata = json.load(open("data.json"))
word = input("Enter word : ").lower()
guesses = get_close_matches(word, mydata.keys()) #list

# Returns a generator about which I am unaware of
# print(mydata.values() for word in mydata.keys()) 
if word in mydata:
    output = mydata[word]
    for item in output:
        print(item)
elif len(guesses)!=0:
    confirmation = input("Did you mean %s instead? Enter Y to continue, else press N: " % guesses[0]).upper() #no comma
    if confirmation == 'Y':
        print(mydata[guesses[0]])
    else:
        print("Please try again")
else:
    print("The word you entered doesn't exist. Please check it again.")

