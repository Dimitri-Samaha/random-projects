from english_words import get_english_words_set
import random as rand

ews = get_english_words_set(["web2"], lower=True, alpha=True)


english_list_words = list(ews)
r = rand.randint(0, len(english_list_words))
word = english_list_words[r]
print(word)

done = False
while not done:
    letter_input = input("Letter: ")
    i = str(word).find(letter_input)
    if i == "-1":
        print("NONO")
    else:
        print(word)
        dine = True

