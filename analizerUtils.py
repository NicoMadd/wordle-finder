from utils import countCharOccurrences, findCharOccurrences

def ponderateWord(word:str,ponderation:dict[(str,float)]) -> float:
    # return 1 / (sum([ponderation[letter] for letter in word]))
    # more ponderation for diverse letter words
    firstPonderation = 1 / (sum([ponderation[letter] for letter in word[0]]))
    secondPonderation = firstPonderation
    for letter in word:
        secondPonderation -= ponderation[letter]*(countCharOccurrences(word,letter)-1)
    return secondPonderation

def ponderateDictionary(dictionary:list[str]):
    occurrences = {}
    for word in dictionary:
        wordOccurrences = findCharOccurrences(word)
        for key, value in wordOccurrences.items():
            if key in occurrences:
                occurrences[key] += value
            else:
                occurrences[key] = value

    values = occurrences.values()
    totalLetters = sum(values)
    informationPonderation = [totalLetters / value for value in values]

    
    ponderatedChars = dict(zip(occurrences.keys(), informationPonderation))

    ponderateWords = [ponderateWord(word,ponderatedChars) for word in dictionary]

    ponderateWords = list(zip(dictionary, ponderateWords))

    print(len(ponderateWords))
    # order list by ponderation

    return sorted(ponderateWords, key=lambda x: x[1], reverse=True)