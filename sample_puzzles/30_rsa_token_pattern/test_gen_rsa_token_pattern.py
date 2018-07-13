from gen_rsa_token_pattern import *

import unittest

class TestTokenConstructors(unittest.TestCase):
    def test_regularTokenLength(self):
        # Regular tokens should be six-digit integers
        # i.e between 100000 999999
        for i in range(1000):
            token = regular()
            self.assertGreaterEqual(token, 100000)
            self.assertLessEqual(token, 999999)

    def test_sixDigitPalindromeLength(self):
        # Palindromic tokens should be six-digit integers
        # i.e between 100000 999999
        for i in range(1000):
            token = pal()
            self.assertGreaterEqual(token, 100000)
            self.assertLessEqual(token, 999999)

    def test_isSixDigitPalindrome(self):
        # palindromic tokens should be integers who're equal to their reverse
        for i in range(1000):
            sixDigitPalindrome = pal()
            self.assertEqual(sixDigitPalindrome, int(str(sixDigitPalindrome)[::-1]))

    def test_miniPalindromeLength(self):
        # mini-palindromic tokens should be six-digit integers
        # i.e between 100000 999999
        for i in range(1000):
            token = mini()
            self.assertGreaterEqual(token, 100000)
            self.assertLessEqual(token, 999999)

    def test_isMiniPalindrome(self):
        # mini-palindromic tokens should be integers whose first
        # and last 3 digits are palindromes
        for i in range(1000):
            miniP = mini()
            palindrome1 = int(str(miniP)[:3])
            palindrome2 = int(str(miniP)[3:])
            self.assertEqual(palindrome1, int(str(palindrome1)[::-1]))
            self.assertEqual(palindrome2, int(str(palindrome2)[::-1]))

    def test_risingTokenLength(self):
        # Rising tokens should be six-digit integers
        # i.e between 100000 999999
        for i in range(1000):
            token = rising()
            self.assertGreaterEqual(token, 100000)
            self.assertLessEqual(token, 999999)

    def test_isRisingToken(self):
        # Each digit in a rising token must be greater than
        # or equal to the digit to the left of it
        for i in range(100000):
            risingToken = str( rising() )
            for i in range( 1, 6 ):
                self.assertGreaterEqual( risingToken[i], risingToken[ i - 1 ] )

    def test_fallingTokenLength(self):
        # Falling tokens should be six-digit integers
        # i.e between 100000 999999
        for i in range(1000):
            token = falling()
            self.assertGreaterEqual(token, 100000)
            self.assertLessEqual(token, 999999)

    def test_isFallingToken(self):
        # Each digit in a falling token must be less than
        # or equal to the digit to the left of it
        for i in range(100000):
            fallingToken = str( falling() )
            for i in range( 1, 6 ):
                self.assertLessEqual( fallingToken[i], fallingToken[ i - 1 ] )

if __name__ == '__main__':
    unittest.main()
