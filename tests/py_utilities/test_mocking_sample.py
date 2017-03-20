import unittest
from pysnips.py_utilities.mocking_sample import rm
import tempfile
import os


class MockingSampleTestCases(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as file:
            file.write(b"DELETE ME!")

    def test_rm(self):
        """>>>> Testing removing a file"""
        rm(self.tmpfilepath)
        # test that the file was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), msg="Failed to remove file")


if __name__ == '__main__':
    unittest.main()
