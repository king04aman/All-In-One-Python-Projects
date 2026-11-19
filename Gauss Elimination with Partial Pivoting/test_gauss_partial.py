import io
import unittest
from contextlib import redirect_stdout

from main import gauss_partial, resolve_matrix


class PartialPivotingTests(unittest.TestCase):
    def test_selects_largest_value_even_when_a_smaller_value_follows(self):
        matrix = [[1, 1, 0, 2], [10, 0, 0, 10], [2, 0, 1, 3]]

        gauss_partial(matrix, 0)

        self.assertEqual(matrix, [[10, 0, 0, 10], [1, 1, 0, 2], [2, 0, 1, 3]])

    def test_keeps_negative_pivot_with_largest_magnitude(self):
        matrix = [[-10, 1, -9], [2, 1, 3]]

        gauss_partial(matrix, 0)

        self.assertEqual(matrix, [[-10, 1, -9], [2, 1, 3]])

    def test_selects_negative_candidate_with_largest_magnitude(self):
        matrix = [[1, 1, 0, 2], [-10, 0, 0, -10], [2, 0, 1, 3]]

        gauss_partial(matrix, 0)

        self.assertEqual(matrix, [[-10, 0, 0, -10], [1, 1, 0, 2], [2, 0, 1, 3]])

    def test_keeps_first_row_when_pivot_magnitudes_are_equal(self):
        matrix = [[-10, 1, -9], [10, 1, 11]]

        gauss_partial(matrix, 0)

        self.assertEqual(matrix, [[-10, 1, -9], [10, 1, 11]])

    def test_only_swaps_rows_in_the_active_submatrix(self):
        matrix = [[100, 100, 0, 200], [0, 1, 1, 2], [0, -10, 1, -9]]

        gauss_partial(matrix, 1)

        self.assertEqual(matrix, [[100, 100, 0, 200], [0, -10, 1, -9], [0, 1, 1, 2]])

    def test_solves_system_with_negative_pivot_and_zero_below_it(self):
        matrix = [[-1, 1, 0], [0, 1, 1]]
        output = io.StringIO()

        with redirect_stdout(output):
            resolve_matrix(matrix)

        self.assertIn('x_0 = 1.0', output.getvalue())
        self.assertIn('x_1 = 1.0', output.getvalue())


if __name__ == '__main__':
    unittest.main()
