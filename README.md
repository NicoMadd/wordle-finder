# Wordle Finder

## English

### Description

This tool was made to find words for the game **Wordle**. Give it a try!

Spanish: https://wordle.danielfrg.com/
English: https://www.powerlanguage.co.uk/wordle/

Have in mind that the game just uses five letter words. But the code also works for any list of words.

### How to

1. First we need to download the wordlist.

There's a method in filesManager to download all files, english and spanish -> set_files

2. Create a WordFinder instance and set the wordlist.

3. Use the WordFinder to filter the wordlist.

### Example find word "human":

    set_files()

    dictionary = get_english_five_letter_words()

    wf = WordFinder(dictionary)

    wf.hasLetters("uan").hasNoLetters("rtzcbfie").hasLetterInPosition("h",1).hasLetterInPosition("a",4).hasLetterInPosition("m",3).hasNoLetterInPosition("m",2)

    print(wf.getWords())

    # Output:
    ['human']

### Search Parser

The search parser sintax is mainly composed by 4 components separated by pipes (|). Each component represents a set of letters that would be in a word. The letters can be upper or lower case, it's not considered in the parser.

An example of search parser:

_wf.parseSearch("artao|hyfb|a2t3|n3r4o2)_

The first set indicates the letters that **ARE** present in the word to search, regardless of their position.

The second set indicates the letters that **ARE NOT** present in the word to search, regardless of their position.

The sintax of the first two sets is very simple. The only difference to keep in mind is that if a letter appears more than once in the first set, it means that it will search for words with n amounts of that letter.

As you can see in the set _"artao"_ we search for words with two a, one t, one o and one r.

The third set indicates the letters that **DO** appear in the word to search in the indicated position.

The fourth set indicates the letters that **DO NOT** appear in the word to search in the indicated position.

The third and fourth sintax gets a bit more complicated with a letter and a number as well. The first letter indicates the letter to search in the word. The number indicates the position of the letter in the word.

#### Example find word "house":

    set_files()

    dictionary = get_english_five_letter_words()

    wf = WordFinder(dictionary)

    # find house
    # piano

    wf = wf.parseSearch("o|pian||p1i2a3n4o5")

    # Output: ['bebog', 'bedog', 'bedot', 'befog', 'begob', 'begod', 'begot', 'below', 'bemol',
    # 'beode', 'berob', 'beroe', 'besom', 'besot', 'bevor', 'byous', 'blobs', 'block', 'blocs',
    # 'bloke', 'blore', 'blote', 'blots', 'blout', 'blowy', 'blows', 'bobby', 'bobet', 'bocce',
    # ... 'wrote', 'wroth', 'xerox', 'xylol', 'zeros', 'zlote', 'zloty', 'zolle', 'zoque']

    # piano -> tower

    wf = wf.parseSearch("oe|piantwr|o2|p1i2a3n4o5t1w3e4r5")

    # Output: ['bocce', 'boche', 'bodge', 'bodle', 'bogle', 'bogue', 'boyce', 'bombe', 'bouge',
    # 'boule', 'bouse', 'bozze', 'coble', 'cocle', 'coeds', 'coeff', 'cogue', 'cohue', 'combe',
    # 'lodge', 'loess', 'louse', 'moble', 'moche', 'modge', 'moeck', 'moyle', 'molge', 'molle',
    # ... 'moule', 'mouse', 'socle', 'solve', 'souse', 'vogue', 'vouge', 'zolle', 'zoque']

    # piano -> tower -> lodge

    wf = wf.parseSearch("oe|piantwrldg|o2e5|p1i2a3n4o5t1w3e4r5l1d3g4")

    # Output: ['bocce', 'boche', 'boyce', 'bombe', 'bouse', 'bozze', 'cohue', 'combe', 'comme',
    # 'coque', 'cosse', 'couve', 'fosse', 'homme', 'house', 'houve', 'youse', 'youve', 'youze',
    # 'joyce', 'moche', 'momme', 'mouse', 'souse', 'zoque']

    # piano -> tower -> lodge -> joyce

    wf = wf.parseSearch("oe|piantwrldgcyj|o2e5|p1i2a3n4o5t1w3e4r5l1d3g4j1y3c4")

    # Output: ['bombe', 'bouse', 'bozze', 'fosse', 'homme', 'house', 'houve', 'momme', 'mouse',
    # 'souse', 'zoque']

    # piano -> tower -> lodge -> joyce -> mouse

    wf = wf.parseSearch("oeus|piantwrldgcyjm|o2e5o2u3|p1i2a3n4o5t1w3e4r5l1d3g4j1y3c4m1")

    # Output: ['bouse', 'house']

    print(wf.getWords())

### TODOs

-   analyze the words and find the best ones to start playing.

    Feel free to contribute!

### Descripcion

Esto fue hecho para encontrar palabras en el juego **Wordle**. ¡Probalo! Abajo el link.

Spanish: https://wordle.danielfrg.com/
English: https://www.powerlanguage.co.uk/wordle/

Tene en cuenta que el juego solo usa palabras de 5 letras. Pero el código también funciona para cualquier lista de palabras.

### Como usarlo

1. Primero necesitamos descargar la lista de palabras.

Hay un metodo en filesManager para descargar todos los archivos, ingles y español -> set_files

2. Crear una instancia de WordFinder y setear la lista de palabras.

3. Usar el WordFinder para filtrar la lista de palabras.

### Ejemplo buscar palabra "raton":

    set_files()

    dictionary = get_spanish_five_letter_words()

    wf = WordFinder(dictionary)

    wf = wf.hasLetters("rot").hasNoLetters("hfdwmeiul").hasLetterInPosition("r",1).hasNoLetterInPosition("h",2).hasLetterInPosition("t",3)

    print(wf.getWords())

    # Output:
    ['raton']

### Parser de busqueda

La sintaxis del parser de busqueda se compone de 4 componentes separados por pipes (|). Cada componente representa un conjunto de letras que corresponderian a una palabra. Las letras pueden ser mayusculas o minusculas, no se contempla eso en el parser.

Un ejemplo de busqueda seria:

_wf.parseSearch("artao|hyfb|a2t3|n3r4o2)_

El primer conjunto indica las letras que **SI** estan presentes en la palabra a buscar sin importar su posicion.

El segundo conjunto indica las letras que **NO** estan presentes en la palabra a buscar sin importar su posicion.

La sintaxis de los primeros dos conjuntos es bastante simple. La unica diferencia a tener en cuenta es que si una letra aparece mas de una vez en
el primer conjunto, significa que se buscaran palabras con n cantidades de esa letra.

Como se puede ver en el conjunto _"artao"_ se buscaran palabras con dos a, una t, una o y una r.

El tercer conjunto indica las letras que **SI** estan presentes en la palabra a buscar en la posicion indicada.

El cuarto conjunto indica las letras que **NO** estan presentes en la palabra a buscar en la posicion indicada.

La sintaxis del tercer y cuarto conjunto se complejiza con una letra y un numero. La letra indica la letra a buscar en la palabra. El numero indica la posicion de la letra dentro de la palabra.

#### Ejemplo buscar palabra "raton":

    set_files()

    dictionary = get_spanish_five_letter_words()

    wf = WordFinder(dictionary)

    # encontrar raton siguiendo una secuencia de palabras
    # piano

    wf = wf.parseSearch("aon|ip||p1i2a3n4o5")

    # Output: ['ambon', 'angor', 'arcon', 'argon', 'armon', 'arzon', 'azcon', 'angor',
    # 'bacon', 'bajon', 'balon', 'baron', 'bayon', 'bonga', 'cagon', 'cajon',
    # 'calon', 'camon', 'caron', 'cason', 'caton', 'cavon', 'cazon', 'conca',
    # 'conga', 'conta', 'coran', 'coyan', 'conac', 'donar', 'facon', 'fajon',
    # 'faron', 'fonda', 'galon', 'gamon', 'gason', 'habon', 'halon', 'haron',
    # 'holan', 'honda', 'honra', 'jabon', 'jalon', 'jamon', 'lacon', 'ladon',
    # 'laton', 'longa', 'lonja', 'macon', 'mahon', 'malon', 'mamon', 'maron',
    # 'mason', 'maton', 'monda', 'monga', 'monja', 'monta', 'coran', 'nocla',
    # 'nodal', 'noema', 'nogal', 'nomas', 'noray', 'norma', 'notar', 'noval',
    # 'novar', 'nocha', 'ondra', 'ornar', 'rabon', 'radon', 'rajon', 'ramon',
    # 'raton', 'rayon', 'razon', 'roman', 'ronca', 'ronda', 'ronza', 'ronal',
    # 'ronar', 'sacon', 'sajon', 'salon', 'sayon', 'sazon', 'sonar', 'sonda',
    # 'sonar', 'tabon', 'tacon', 'tafon', 'tajon', 'talon', 'tanor', 'taxon',
    # 'tazon', 'tonal', 'tonar', 'tonca', 'tonga', 'vagon', 'valon', 'varon',
    # 'zafon', 'zahon', 'zajon', 'zonal', 'zonda']

    # piano -> honra

    wf = wf.parseSearch("aonr|iph||p1i2a3n4o5h1o2n3r4a5")

    # Output: ['angor', 'arcon', 'argon', 'armon', 'arzon', 'angor', 'baron', 'caron',
    # 'faron', 'maron', 'rabon', 'radon', 'rajon', 'ramon', 'raton', 'rayon',
    # 'razon', 'varon']

    # piano -> honra -> armon

    wf = wf.parseSearch("aonr|iphm|o4n5|p1i2a3n4o5h1o2n3r4a5a1r2m3")

    # Output: ['baron', 'caron', 'faron', 'rabon', 'radon', 'rajon', 'raton', 'rayon',
    # 'razon', 'varon']

    # piano -> honra -> armon -> rabon

    wf = wf.parseSearch("aonr|iphmb|o4n5r1a2|p1i2a3n4o5h1o2n3r4a5a1r2m3b3")

    # Output: ['radon', 'rajon', 'raton', 'rayon', 'razon']

    print(wf.getWords())

### TODOs

-   analizar las palabras y encontrar las mejores para comenzar a jugar.

    Sientanse libres de colaborar! :)
