# -*- codgin: utf-8 -*-
"""
Calculate the date of meetups.

Typically meetups happen on the same day of the week.

Examples are

- the first Monday
- the third Tuesday
- the Wednesteenth
- the last Thursday

Note that "Monteenth", "Tuesteenth", etc are all made up words. There
was a meetup whose members realised that there are exactly 7 days that
end in '-teenth'. Therefore, one is guaranteed that each day of the week
(Monday, Tuesday, ...) will have exactly one date that is named with '-teenth'
in every month.
"""
import unittest
from datetime import date

from algorithms.meetup import meetup_day


class MeetupTest(unittest.TestCase):
    def test_monteenth_of_may_2013(self):
        self.assertEqual(date(2013, 5, 13),
                         meetup_day(2013, 5, 'Monday', 'teenth'))

    def test_saturteenth_of_february_2013(self):
        self.assertEqual(date(2013, 2, 16),
                         meetup_day(2013, 2, 'Saturday', 'teenth'))

    def test_first_tuesday_of_may_2013(self):
        self.assertEqual(date(2013, 5, 7),
                         meetup_day(2013, 5, 'Tuesday', '1st'))

    def test_second_monday_of_april_2013(self):
        self.assertEqual(date(2013, 4, 8),
                         meetup_day(2013, 4, 'Monday', '2nd'))

    def test_third_thursday_of_september_2013(self):
        self.assertEqual(date(2013, 9, 19),
                         meetup_day(2013, 9, 'Thursday', '3rd'))

    def test_fourth_sunday_of_march_2013(self):
        self.assertEqual(date(2013, 3, 24),
                         meetup_day(2013, 3, 'Sunday', '4th'))

    def test_last_thursday_of_october_2013(self):
        self.assertEqual(date(2013, 10, 31),
                         meetup_day(2013, 10, 'Thursday', 'last'))

    def test_last_wednesday_of_february_2012(self):
        self.assertEqual(date(2012, 2, 29),
                         meetup_day(2012, 2, 'Wednesday', 'last'))

    def test_last_wednesday_of_december_2014(self):
        self.assertEqual(date(2014, 12, 31),
                         meetup_day(2014, 12, 'Wednesday', 'last'))

    def test_last_sunday_of_only_four_week_february_2015(self):
        self.assertEqual(date(2015, 2, 22),
                         meetup_day(2015, 2, 'Sunday', 'last'))

    def test_first_friday_of_december_2012(self):
        self.assertEqual(date(2012, 12, 7),
                         meetup_day(2012, 12, 'Friday', '1st'))

    def test_fifth_monday_of_march_2015(self):
        self.assertEqual(date(2015, 3, 30),
                         meetup_day(2015, 3, 'Monday', '5th'))


if __name__ == '__main__':
    unittest.main()
