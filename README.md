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

    wf.hasLetters("uan").hasNoLetters("rtzcbfie").hasLetterInPosition("h",1).hasLetterInPosition("a",4).hasLetterInPosition("m",3)

    print(wf.getWords())

    # Output:
    ['human']

### TODOs

-   add input method to parse the search word -> example -> find("h-m--") -> all words with h and m and in those positions. Would also be interesting to filter the odd letters out.
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

    wf.hasLetters("rot").hasNoLetters("hfdwmeiu").hasLetterInPosition("r",1).hasLetterInPosition("n",5)

    print(wf.getWords())

    # Output:
    ['raton']

### TODOs

-   agregar una opcion para que el usuario pueda ingresar una palabra y que el programa la busque. -> find("h-m--") -> todas las palabras que tienen h y m y en esas posiciones. Tambien se podria filtrar las letras impares.
-   analizar las palabras y encontrar las mejores para comenzar a jugar.

    Sientanse libres de colaborar! :)
