from wordFinder import WordFinder
from utils import *
from filesManager import *

if __name__=="__main__":

    set_files()

    dictionary = get_spanish_five_letter_words()

    wf = WordFinder(dictionary)
    
    # try it!
    
    wf = wf.parseSearch("aib|plzoyudnegrchv|a5i2|a1a3i3")
    
    print(wf.getWords())
    