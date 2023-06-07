import unittest

from src.rover import Rover


class MarsRoverTests(unittest.TestCase):
    def test_move_forward_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.forward()
        self.assertEqual(rover.coordinates, [4, 8])

    def test_move_forward_facing_east(self):
        rover = Rover([4, 7], 'E')
        rover.forward()
        self.assertEqual(rover.coordinates, [5, 7])

    def test_move_forward_facing_west(self):
        rover = Rover([4, 7], 'W')
        rover.forward()
        self.assertEqual(rover.coordinates, [3, 7])

    def test_move_forward_facing_south(self):
        rover = Rover([4, 7], 'S')
        rover.forward()
        self.assertEqual(rover.coordinates, [4, 6])

    def test_move_backward_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.backwards()
        self.assertEqual(rover.coordinates, [4, 6])

    def test_move_backward_facing_east(self):
        rover = Rover([4, 7], 'E')
        rover.backwards()
        self.assertEqual(rover.coordinates, [3, 7])

    def test_move_backward_facing_west(self):
        rover = Rover([4, 7], 'W')
        rover.backwards()
        self.assertEqual(rover.coordinates, [5, 7])

    def test_move_backward_facing_south(self):
        rover = Rover([4, 7], 'S')
        rover.backwards()
        self.assertEqual(rover.coordinates, [4, 8])

    def test_move_forward_twice_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.forward()
        rover.forward()
        self.assertEqual(rover.coordinates, [4, 9])

    def test_turn_right_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.rotate('R')
        self.assertEqual(rover.direction, 'E')

    def test_turn_left_facing_north(self):
        rover = Rover([4, 7], 'N')
        rover.rotate('L')
        self.assertEqual(rover.direction, 'W')

    def test_turn_right_facing_east(self):
        rover = Rover([4, 7], 'E')
        rover.rotate('R')
        self.assertEqual(rover.direction, 'S')

    def test_run_left_facing_east(self):
        rover = Rover([4, 7], 'E')
        rover.rotate('L')
        self.assertEqual(rover.direction, 'N')

    def test_turn_right_facing_south(self):
        rover = Rover([4, 7], 'S')
        rover.rotate('R')
        self.assertEqual(rover.direction, 'W')

    def test_turn_left_facing_south(self):
        rover = Rover([4, 7], 'S')
        rover.rotate('L')
        self.assertEqual(rover.direction, 'E')

    def test_turn_and_move(self):
        rover = Rover([4, 7], 'N')
        rover.rotate('R')
        rover.forward()
        self.assertEqual(rover.direction, 'E')
        self.assertEqual(rover.coordinates, [5, 7])

    def test_move_and_turn(self):
        rover = Rover([4, 7], 'W')
        rover.forward()
        rover.rotate('L')
        self.assertEqual(rover.direction, 'S')
        self.assertEqual(rover.coordinates, [3, 7])

if __name__ == '__main__':
    unittest.main()
