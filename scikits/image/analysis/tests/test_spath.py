import numpy as np
from numpy.testing import *

from scikits.image.analysis import shortest_path

class TestShortestPath:
    def test_basic(self):
        x = np.array([[1, 1, 3],
                      [0, 2, 0],
                      [4, 3, 1]])
        y = np.empty((3,))
        path, cost = shortest_path(x)
        assert_array_equal(path, [0, 0, 1])
        assert_equal(cost, 1)

if __name__ == "__main__":
    run_module_suite()
