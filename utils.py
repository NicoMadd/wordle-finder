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
        outfile.write(req.text)

def read_file(file_name):
    with open(file_name, "r",encoding="utf-8") as f:
        data = f.read()
    return data

def file_exists(file_name):
    return os.path.isfile(file_name)

def write_file(file_name, data):
    with open(file_name, "w",encoding="utf-8") as f:
        f.write(data)
        
def write_file_as_json(file_name, data):
    with open(file_name, "w",encoding="utf-8") as f:
        json.dump(data, f)
        
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')