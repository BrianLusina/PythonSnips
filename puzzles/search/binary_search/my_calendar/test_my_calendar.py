import unittest

from . import MyCalendar


class MyCalendarTestCase(unittest.TestCase):
    def test_1(self):
        """should return [null, true, false, true] for  MyCalendar().book(10,20) -> MyCalendar().book(15,25), MyCalendar().book(20,30)"""
        my_calendar = MyCalendar()

        first_booking = my_calendar.book(10, 20)
        self.assertTrue(first_booking)

        second_booking = my_calendar.book(15, 25)
        self.assertFalse(second_booking)

        third_booking = my_calendar.book(20, 30)
        self.assertTrue(third_booking)


if __name__ == "__main__":
    unittest.main()
