from utils import *
import unidecode

ENGLISH_ALL_WORDS_FILE = "all_english_words.json"
ENGLISH_FIVE_LETTER_WORD_FILE = "five_letter_words_english.json"
ENGLISH_WORDS_FILE_COMPLETE = "raw_all_english_words.txt"
SPANISH_WORDS_FILE = "all_spanish_words.json"
SPANISH_FIVE_LETTER_WORD_FILE = "five_letter_words_spanish.json"

def format_spanish_words(reqText:str):
    reqText = reqText.lower()
    reqText = unidecode.unidecode(reqText)
    return reqText.split("\n")
    
def format_english_words(reqText:str):
    reqText = reqText.lower()
    reqText = unidecode.unidecode(reqText)
    return list(json.loads(reqText).keys())    

def download_complete_english_file():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    download_file_as_txt(url, ENGLISH_WORDS_FILE_COMPLETE)

def download_english_main_file():
    
    # repo with all english words
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"

    # download file
    # write text to file as json so you dont have to make multiple requests each time you run the code
    download_file_as_json(url, ENGLISH_ALL_WORDS_FILE,preformat=format_english_words)

def download_spanish_main_file():
    url = "https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt"
    download_file_as_json(url, SPANISH_WORDS_FILE,preformat=format_spanish_words)

def make_spanish_five_letter_word_file():
    
    # get all words
    all_words:list = get_spanish_all_words()
    
    # filter five letter words
    five_letter_words:list = [word for word in all_words if len(word) == 5 ]

    # same as before, save a file with the five letter words, better performance

    write_file_as_json(SPANISH_FIVE_LETTER_WORD_FILE,five_letter_words)

def make_english_five_letter_word_file():
    
    # get all words
    all_words:list = get_english_all_words()
    
    # filter five letter words
    five_letter_words:list = [word for word in all_words if len(word) == 5 ]

    write_file_as_json(ENGLISH_FIVE_LETTER_WORD_FILE,five_letter_words)
    
def get_english_five_letter_words() -> list:
    data = read_file(ENGLISH_FIVE_LETTER_WORD_FILE)
    return json.loads(data)

def get_spanish_five_letter_words() -> list:
    data = read_file(SPANISH_FIVE_LETTER_WORD_FILE)
    return json.loads(data)
    
def get_spanish_all_words() -> list:
    data = read_file(SPANISH_WORDS_FILE)
    return json.loads(data)

def get_english_all_words() -> list:
    data = read_file(ENGLISH_ALL_WORDS_FILE)
    return json.loads(data)
    
def set_files():
    download_english_main_file()
    make_english_five_letter_word_file()
    
    download_spanish_main_file()
    make_spanish_five_letter_word_file()
    
    