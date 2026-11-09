"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1
import math

class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("Apple"),2)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""),0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
         self.assertEqual(hw1.short_lists([[1], [2, 3, 2], [], [4, 5, 6], [7, 8, 4]]),[])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]),[[2, 3], [7, 8]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[2,6], [6,2], [5,5]]), [[2,6], [2,6], [5,5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[2,6,3], [6,2,1], [5,2]]), [[2,6,3], [6,2,1], [2,5]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices((data.Price(3,0)),(data.Price(5,0))),data.Price(8, 0))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices((data.Price(3,50)),(data.Price(5,40))),data.Price(8, 90))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(2,3), data.Point(7,0))), 15)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-6,5), data.Point(10,-1))), 96)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book_one = data.Book(["Dr Seuss"], "The Cat in the Hat")
        book_two = data.Book(["Matt Dinniman"], "Dungeon Crawler Carl")
        book_three = data.Book(["Dr Seuss"], "Green Eggs and Ham")
        books = [book_one, book_two, book_three]
        self.assertEqual(hw1.books_by_author("Dr Seuss", books), [book_one, book_three])


    def test_books_by_author_no_matches(self):
        book_one = data.Book(["Dr Seuss"], "The Cat in the Hat")
        book_two = data.Book(["Matt Dinniman"], "Dungeon Crawler Carl")
        book_three = data.Book(["Dr Seuss"], "Green Eggs and Ham")
        books = [book_one, book_two, book_three]
        self.assertEqual(hw1.books_by_author("Random Person", books), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(0, 10), data.Point(10, 0))), data.Circle(data.Point(5, 5), math.sqrt(50)))
    def test_circle_bound_non_square_rectangle(self):
    #     # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.assertEqual(hw1.circle_bound(data.Rectangle(data.Point(2, 6), data.Point(8, 2))), data.Circle(data.Point(5, 4), math.sqrt(13)))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [
            data.Employee("Alice", 10),
            data.Employee("Bob", 20),
            data.Employee("Cara", 30),
        ]
        self.assertEqual(hw1.below_pay_average(employees), ["Alice"])

    def test_below_pay_average_empty_list(self):
         self.assertEqual(hw1.below_pay_average([]), [])

if __name__ == '__main__':
    unittest.main()
