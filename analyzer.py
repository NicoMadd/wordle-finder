import matplotlib.pyplot as plt
from analizerUtils import ponderateDictionary
from filesManager import *
from wordFinder import WordFinder

dictionary = get_spanish_five_letter_words()

print(len(dictionary))
wf = WordFinder(dictionary).parseSearch("ndal|o||")

dictionary = wf.getWords()
ponderatedWords = ponderateDictionary(dictionary)

# print(dictionary)
print(ponderatedWords[:10])



# plt.bar(occurrences.keys(), occurrences.values())
# plt.show()