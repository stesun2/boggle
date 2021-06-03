from boggle_board import BoggleBoard 
import unittest

class BoggleBoardTestCase(unittest.TestCase):

    def test_initial_board_size(self):
        bb = BoggleBoard()
        self.assertEqual(len(bb.board),16)

    def test_random_board(self):
        bb = BoggleBoard(custom_seed = 7)

    


if __name__ == '__main__':
    unittest.main()