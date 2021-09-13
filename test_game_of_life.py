import unittest
from game_of_life import count_neighbors


state0 = [[0,0,0],
          [0,0,0],
          [0,0,0]]

state1 = [[1,1,1],
          [1,1,1],
          [1,1,1]]

state2 = [[0,0,0],
          [0,1,0],
          [0,0,0]]

state3 = [[1,0,1],
          [0,0,0], 
          [1,0,1]]

state4 = [[0,1,0],
          [1,0,1],
          [0,1,0]]

state5 = [[0,1,0],
          [1,1,1],
          [0,1,0]]


class TestGameOfLife(unittest.TestCase):

    def test_count_neighbors(self):
        # center
        self.assertEqual(count_neighbors(state0, 1, 1), 0)
        self.assertEqual(count_neighbors(state1, 1, 1), 8)
        self.assertEqual(count_neighbors(state2, 1, 1), 0)
        self.assertEqual(count_neighbors(state3, 1, 1), 4)
        self.assertEqual(count_neighbors(state4, 1, 1), 4)
        # corners
        self.assertEqual(count_neighbors(state4, 0, 0), 2)
        self.assertEqual(count_neighbors(state4, 2, 0), 2)
        self.assertEqual(count_neighbors(state4, 0, 2), 2)
        self.assertEqual(count_neighbors(state4, 2, 2), 2)
        # sides
        self.assertEqual(count_neighbors(state3, 1, 0), 2)
        self.assertEqual(count_neighbors(state3, 0, 1), 2)
        self.assertEqual(count_neighbors(state3, 2, 1), 2)
        self.assertEqual(count_neighbors(state3, 1, 2), 2)


if __name__ == '__main__':
    unittest.main()
