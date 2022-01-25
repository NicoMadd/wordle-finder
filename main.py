from wordFinder import WordFinder
from utils import *
from filesManager import *

if __name__=="__main__":

    set_files()
    
    dictionary = get_english_five_letter_words()
    
    wf = WordFinder(dictionary)

    # # example
    # words = wf.hasLetters(split("nol")).hasNoLetters(split("eighvautfy")).hasLetterInPosition("l",4).getWords()

    print(words)
    
    
    
    
    
    # palabras_cinco_letras = [palabra for palabra in palabras if len(palabra) == 5]
    
    # print(palabras_cinco_letras)
    
    # download_file(file_name="palabras.txt", url="https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt")
    # write_file_as_json("palabras.json",data)
    
