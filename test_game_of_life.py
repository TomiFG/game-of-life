import unittest
from game_of_life import count_neighbors, next_state


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

    def test_next_state(self):

        expected_output_s0 = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
                ]

        actual_output_s0 = next_state(state0)
        self.assertEqual(expected_output_s0, actual_output_s0)

        expected_output_s1 = [
                [1,0,1],
                [0,0,0],
                [1,0,1]
                ]

        actual_output_s1 = next_state(state1)
        self.assertEqual(expected_output_s1, actual_output_s1)

        expected_output_s2 = [
                [0,0,0],
                [0,0,0],
                [0,0,0]
                ]

        actual_output_s2 = next_state(state2)
        self.assertEqual(expected_output_s2, actual_output_s2)

        expected_output_s3 = [
                [0,0,0],
                [0,0,0], 
                [0,0,0]
                ]

        actual_output_s3 = next_state(state3)
        self.assertEqual(expected_output_s3, actual_output_s3)

        expected_output_s4 = [
                [0,1,0],
                [1,0,1],
                [0,1,0]
                ]

        actual_output_s4 = next_state(state4)
        self.assertEqual(expected_output_s4, actual_output_s4)

        expected_output_s5 = [
                [1,1,1],
                [1,0,1],
                [1,1,1]
                ]

        actual_output_s5 = next_state(state5)
        self.assertEqual(expected_output_s5, actual_output_s5)
        


if __name__ == '__main__':
    unittest.main()
