import unittest
from main import Guess_Game

class TestGameMethods(unittest.TestCase):

    def test_input(self):
        testGame = Guess_Game()
        guess = testGame.get_input()
        self.assertTrue(guess % 2 != 0)
    
    def test_answer(self):
        testGame = Guess_Game()
        answer = testGame.get_answer()
        self.assertTrue(answer % 2 != 0)

if __name__ == '__main__':
    unittest.main()
