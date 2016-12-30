# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

words = ['cat', 'dog', 'rabbit']
letters = []

for word in words:
    for letter in word:
        if letter not in letters:
            letters.append(letter)

print(letters)
