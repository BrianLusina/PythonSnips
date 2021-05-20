import unittest

from algorithms.graphs.roads_and_libs import roads_and_libraries


class RoadsAndLibrariesTestCase(unittest.TestCase):
    def test_3_cities_with_c_road_as_1_and_c_lib_as_2(self):
        n = 3
        c_lib = 2
        c_road = 1
        cities = [[1, 2], [3, 1], [2, 3]]
        actual = roads_and_libraries(n, c_lib, c_road, cities)
        expected = 4
        self.assertEqual(expected, actual)

    def test_6_cities_with_c_road_as_5_and_c_lib_as_2(self):
        n = 6
        c_lib = 2
        c_road = 5
        cities = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
        actual = roads_and_libraries(n, c_lib, c_road, cities)
        expected = 12
        self.assertEqual(expected, actual)

    def test_6_cities_with_c_road_as_3_and_c_lib_as_2(self):
        n = 6
        c_lib = 2
        c_road = 3
        cities = [[1, 2], [1, 3], [4, 5], [4, 6]]
        actual = roads_and_libraries(n, c_lib, c_road, cities)
        expected = 12
        self.assertEqual(expected, actual)

    def test_5_cities_with_c_road_as_1_and_c_lib_as_6(self):
        n = 5
        c_lib = 6
        c_road = 1
        cities = [[1, 2], [1, 3], [1, 4]]
        actual = roads_and_libraries(n, c_lib, c_road, cities)
        expected = 15
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
