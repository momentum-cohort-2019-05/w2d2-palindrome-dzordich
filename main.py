words = input("Please enter a string to test if it is a palidrome ")
letters = "abcdefghijklmnopqrstuvwxyz"
words = words.lower()
forward = []
backward = []

for char in words:
    if char in letters:
        forward.append(char)
        backward.append(char)
backward.reverse()

if forward == backward:
    print(words + " is a palidrome!")
else:
    print(words + " is not a palidrome.")



# def addToList(char):
