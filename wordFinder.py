


class WordFinder:

    def __init__(self, wordList:list):
        self.originalWordList:list = wordList
        self.filteredWordList:list = wordList
        
    def hasLetter(self,letter:str):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word]
        return self
        
    def hasLetterInPosition(self,letter:str,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter in word[position-1]]
        return self
    
    def hasNoLetter(self,letter:str):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word]
        
    def hasNoLetterInPosition(self,letter:str,position:int):
        self.filteredWordList = [word for word in self.filteredWordList if letter not in word[position-1]]
        return self
    
    def hasLetters(self,letters:list[str]):
        for letter in letters:
            self = self.hasLetter(letter) or self
        return self
    
    def hasNoLetters(self,letters:list[str]):
        for letter in letters:
            self = self.hasNoLetter(letter) or self
        return self
    
    def getWords(self) -> list:
        return self.filteredWordList