"""
distribution.py
Author: Billy
Credit: http://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-in-python-based-on-an-attribute-of-the-objects, http://stackoverflow.com/questions/2587402/sorting-python-list-based-on-the-length-of-the-string

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
userInput = input("Please enter a string of text (the bigger the better): ")
userInput = userInput.lower()

characters = {"a":"","b":"","c":"","d":"","e":"","f":"","g":"","h":"","i":"","j":"","k":"","l":"","m":"","n":"","o":"","p":"","q":"","r":"","s":"","t":"","u":"","v":"","w":"","x":"","y":"","z":""}
inputList = []

for s in userInput:
    if s != " " and s != "," and s != "?" and s != "!" and s != "." and s != "'":
        characters[s]+=s
print(len(userInput))
"""
for s in characters[s]:
    if s == len(userInput):
        print(characters[s])


characters.sort(lambda x,y: cmp(len(x), len(y))) 
"""
charlist = []
for key in characters:
    if len(characters[key]) > 0:
        charlist.append(characters[key])
    

charlist.sort()
print(charlist)

for l in range(len(userInput),0,-1):
    print(l)

"""
print(characters)
    
for i in characters:
    if characters[i] != "":
        print(characters[i])
"""

"""
for i in userInput:
    if i != ' ':
        inputList.append(i)

for s in userInput:
    if s == "a":
        print('a')

print(inputList)

a = userInput.count('a')
print(a)  

userInput.count('a')
userInput.count('b')
userInput.count('c')    
userInput.count('d')
userInput.count('e')
userInput.count('f')
userInput.count('g')
userInput.count('h')
userInput.count('i')
userInput.count('j')
userInput.count('k')
userInput.count('l')
userInput.count('m')
userInput.count('n')
userInput.count('o')
userInput.count('p')
userInput.count('q')
userInput.count('r')
userInput.count('s')
userInput.count('t')
userInput.count('u')
userInput.count('v')
userInput.count('w')
userInput.count('x')
userInput.count('y')
userInput.count('z')
"""
