words = input("Please enter a string to test if it is a palidrome ")
letters = "abcdefghijklmnopqrstuvwxyz"
words = words.lower()
forward = []
backward = []
count = 0

def addLetters(place):
    if place < len(words):
        if words[place] in letters:
            forward.append(words[place])
            backward.insert(0, words[place])
        place += 1
        addLetters(place)

addLetters(count)

print(forward)
print(backward)

if forward == backward:
    print(words + " is a palidrome!")
else:
    print(words + " is not a palidrome.")
