from wordFinder import WordFinder
from utils import *
from filesManager import *

if __name__=="__main__":

    set_files()

    dictionary = get_english_five_letter_words()

    wf = WordFinder(dictionary)
    
    # try it!
    
    print(wf.getWords())
    