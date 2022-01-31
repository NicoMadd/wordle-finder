from ast import Return
from utils import countCharOccurrences, findCharOccurrences


class WordFinder:

    def __init__(self, wordList:list):
        self.originalWordList:list = wordList
        self.filteredWordList:list = wordList
    
    def hasLetterNTimes(self,letter:str,n:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word and countCharOccurrences(word,letter) == n]
        return self
    
    def hasLetter(self,letter:str):
        return self.hasLetterNTimes(letter,1)
        
    def hasLetterInPosition(self,letter:str,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word[position-1]]
        return self
    
    def hasNoLetter(self,letter:str):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word]
        
    def hasNoLetterInPosition(self,letter:str,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word[position-1]]
        return self
    
    def hasLetters(self,letters:list[str]):
        occurrences = findCharOccurrences(letters)
        for letter in occurrences:
            self = self.hasLetterNTimes(letter,occurrences[letter])
        return self
    
    def hasNoLetters(self,letters:list[str]):
        for letter in letters:
            self = self.hasNoLetter(letter) or self
        return self
    
    def getWords(self) -> list:
        return self.filteredWordList
    
    def parseSearch(self,search:str):
        search = search.lower()
        hasLetters,hasNoLetters, lettersInPosition, noLettersInPosition = search.split("|")
        
        lettersInPositionPairs = [lettersInPosition[i:i+2] for i in range(0, len(lettersInPosition), 2)]
        noLettersInPositionPairs = [noLettersInPosition[i:i+2] for i in range(0, len(noLettersInPosition), 2)]
        
        
        self = self.hasLetters(hasLetters)
        self = self.hasNoLetters(hasNoLetters)
        for pair in lettersInPositionPairs:
            self = self.hasLetterInPosition(pair[0],int(pair[1]))
            
        for pair in noLettersInPositionPairs:
            self = self.hasNoLetterInPosition(pair[0],int(pair[1]))
        
        return self