import unittest

#IS PALINDROME
def is_palindrome(word):
    index = 0
    backwards = ''
    while index < len(word):
        index += 1
        backwards = backwards + word[-(index)]
    if word == backwards:
        return True
    return False

#IS PALINDROME (FOR VERSION)
def is_palindrome_for(word):
    index = 0
    rev_index = 0
    for index in range(len(word)):
        rev_index = -(index + 1)
        if word[index] != word[rev_index]:
            return False
    return True

#PALINDROME NUMBER
def palindrome_number(words):
    palindromes = 0
    for word in words:
        clean_word = ''.join(character.lower() for character in word if character.isalpha())
        if is_palindrome_for(clean_word):
            palindromes += 1
    return palindromes

#TESTS IS PALINDROME
class TestIsPalindrome(unittest.TestCase):
    def test_a(self):
        input = 'a'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_ala(self):
        input = 'ala'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_neuquen(self):
        input = 'neuquen'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_hola(self):
        input = 'hola'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertFalse(result)
        self.assertFalse(result_for)

    def test_123(self):
        input = '123'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertFalse(result)
        self.assertFalse(result_for)

    def test_777(self):
        input = '777'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_parangaricutimiricuaro(self):
        input = 'parangaricutimiricuaro'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertFalse(result)
        self.assertFalse(result_for)

    def test_anana(self):
        input = 'anana'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_solos(self):
        input = 'solos'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertTrue(result)
        self.assertTrue(result_for)

    def test_giganotosaurus(self):
        input = 'giganotosaurus'
        result = is_palindrome(input)
        result_for = is_palindrome_for(input)
        self.assertFalse(result)
        self.assertFalse(result_for)

#TESTS PALINDROME NUMBER
class TestPalindromeNumber(unittest.TestCase):
    #Se considera palíndromo cuando todo el string se lee igual al derecho y al revés.
    #Deben eliminarse los espacios y símbolos. Ej: 'A man, a plan, a canal - Panama'

    def test_simple1word(self):
        words = ['ala']
        result = palindrome_number(words)
        self.assertEqual(result, 1)

    def test_simple2words(self):
        words = ['ala', 'neuquen']
        result = palindrome_number(words)
        self.assertEqual(result, 2)

    def test_simple3words(self):
        words = ['ala', 'neuquen', 'hola']
        result = palindrome_number(words)
        self.assertEqual(result, 2)

    def test_simple4words(self):
        words = ['ala', 'neuquen', 'hola', 'programación']
        result = palindrome_number(words)
        self.assertEqual(result, 2)

    def test_simple5words(self):
        words = ['ala', 'neuquen', 'hola', 'programación', 'palap']
        result = palindrome_number(words)
        self.assertEqual(result, 3)

    def test_complex6words(self):
        words = ['ala', 'neuquen', 'hola', 'programación', 'palap', 'neu quen']
        result = palindrome_number(words)
        self.assertEqual(result, 4)

    def test_complex9words(self):
        words = [
            'ala',
            'neuquen',
            'hola',
            'programación',
            'palap',
            'neu quen',
            'agita falsos usos la fatiga',
            'presidente de la cámara de diputados: martin menem',
            'A man, a plan, a canal - Panama'
            ]
        result = palindrome_number(words)
        self.assertEqual(result, 6)

unittest.main()