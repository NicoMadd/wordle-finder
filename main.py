from wordFinder import WordFinder
from utils import *

if __name__=="__main__":
    
    # if you want to download the main file, uncomment this
    if(file_exists(ALL_WORDS_FILE) == False):
        download_main_file()
    
    # if you want to make the five letter word file, uncomment this
    if(file_exists(FIVE_LETTER_WORD_FILE) == False):
        make_five_letter_word_file()
    
    

    wf = WordFinder(get_five_letter_words())

    words = wf.hasLetters(split("nol")).hasNoLetters(split("eighvautfy")).hasLetterInPosition("l",4).getWords()

    print(words)

