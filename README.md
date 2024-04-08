# Juan Alejo Patiño - Palíndromos

##### Los palíndromos son palabras, frases o números que se leen igual tanto de izquierda a derecha como viceversa. Es decir, secuencias idénticas incluso tras invertirlas. Algunos palíndromos podrían ser las palabras 'reconocer', 'anilina', 'Neuquén', 'salas', etc.

### El archivo `palindromes.py` contiene las siguientes funciones con sus respectivos tests:

#### `is_palindrome`
##### Comprueba si un string es un palíndromo, invirtiendo el string y comparando si es igual al original.

#### `is_palindrome_for`
##### Comprueba si un string es un palíndromo, comparando que cada carácter del string sea igual al que se encuentra en su posición inversa.

#### `palindrome_number`
##### Limpia el string eliminando todos los caracteres que no sean letras, transforma todos los que sí lo sean en minúsculas, y comprueba la cantidad de palíndromos dentro del string por medio de la función `is_palindrome_for`.