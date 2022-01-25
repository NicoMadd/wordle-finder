import requests, json,os

ALL_WORDS_FILE = "all_english_words.json"
FIVE_LETTER_WORD_FILE = "five_letter_words.json"

def split(word):
    return [char for char in word]

def download_main_file():
    
    # repo with all english words
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"

    # download file
    req = requests.get(url)
    txt = req.text

    # write text to file as json so you dont have to make multiple requests each time you run the code
    with open(ALL_WORDS_FILE, 'w') as outfile:
        json.dump(txt, outfile)

def make_five_letter_word_file():
    
    # get all words
    all_words:list = read_all_words()
    
    # filter five letter words
    five_letter_words:list = [word for word in all_words if len(word) == 5 ]

    # same as before, save a file with the five letter words, better performance
    five_letter_words_json = json.dumps(five_letter_words)

    with open(FIVE_LETTER_WORD_FILE, "w") as f:
        f.write(five_letter_words_json)
    
def get_five_letter_words():
    with open(FIVE_LETTER_WORD_FILE, "r") as f:
        data = f.read()
    five_letter_words:list = json.loads(data)
    return five_letter_words


def get_all_words():
    with open(ALL_WORDS_FILE, "r") as f:
        data = f.read()
    all_words:list = json.loads(data)
    return all_words

def file_exists(file_name):
    return os.path.isfile(file_name)