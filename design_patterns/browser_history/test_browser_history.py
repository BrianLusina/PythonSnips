import unittest

from . import BrowserHistory


class BrowserHistoryTestCases(unittest.TestCase):
    def test_browser_history_sequence_of_steps(self):
        # leetcode.com is set as the home page
        browser_history = BrowserHistory("leetcode.com")

        # You are in "leetcode.com". Visit "google.com"
        browser_history.visit("google.com")

        # You are in "google.com". Visit "facebook.com"
        browser_history.visit("facebook.com")

        # You are in "facebook.com". Visit "youtube.com"
        browser_history.visit("youtube.com")

        # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        history_one = browser_history.back(1)
        self.assertEqual(history_one, "facebook.com")

        # You are in "facebook.com", move back to "google.com" return "google.com"
        history_two = browser_history.back(1)
        self.assertEqual(history_two, "google.com")

        # You are in "google.com", move forward to "facebook.com" return "facebook.com"
        history_three = browser_history.forward(1)
        self.assertEqual(history_three, "facebook.com")

        # You are in "facebook.com". Visit "linkedin.com"
        browser_history.visit("linkedin.com")

        # You are in "linkedin.com", you cannot move forward any steps.
        history_four = browser_history.forward(2)
        self.assertEqual(history_four, "linkedin.com")

        # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        history_five = browser_history.back(2)
        self.assertEqual(history_five, "google.com")

        # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
        history_six = browser_history.back(7)
        self.assertEqual(history_six, "leetcode.com")


if __name__ == "__main__":
    unittest.main()
