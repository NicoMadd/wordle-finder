import requests, json,os,unicodedata

def split(word):
    return [char for char in word]

def download_file_as_json(url, file_name,preformat=lambda x:x):
    req = requests.get(url)
    txt = preformat(req.text)
    with open(file_name, 'w') as outfile:
        json.dump(txt, outfile)
        
def download_file_as_txt(url, file_name,preformat=lambda x:x):
    req = requests.get(url)
    txt = preformat(req.text)
    with open(file_name, 'w') as outfile:
        outfile.write(txt)

def read_file(file_name):
    with open(file_name, "r",encoding="utf-8") as f:
        data = f.read()
    return data

def file_exists(file_name) -> bool:
    return os.path.isfile(file_name)

def write_file(file_name, data):
    with open(file_name, "w",encoding="utf-8") as f:
        f.write(data)
        
def write_file_as_json(file_name, data):
    with open(file_name, "w",encoding="utf-8") as f:
        json.dump(data, f)
        
def strip_accents(s) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def countCharOccurrences(word:str, char:str) -> int:
    return sum(1 for c in word if c == char)

def findCharOccurrences(word:str) -> list:
    return {letter:countCharOccurrences(word,letter) for letter in word}