from copyreg import constructor

from numpy import char


class WordFinder:

    def __init__(self, wordList):
        self.originalWordList = wordList
        self.filteredWordList = wordList
        
    def hasLetter(self,letter:char):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word]
        return self
        
    def hasLetterInPosition(self,letter:char,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word[position-1]]
        return self
    
    def hasNoLetter(self,letter:char):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word]
        
    def hasNoLetterInPosition(self,letter:char,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word[position-1]]
        
    def hasLetters(self,letters:list[str]):
        for letter in letters:
            self = self.hasLetter(letter)
        return self
    
    def hasNoLetters(self,letters:list[str]):
        for letter in letters:
            self = self.hasNoLetter(letter) or self
        return self
    
    def getWords(self):
        return self.filteredWordList