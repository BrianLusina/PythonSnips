#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pysnips.py_utilities.mocking_sample import RemovalService
import tempfile
import os
from mock import patch


class MockingSampleTestCases(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as file:
            file.write(b"DELETE ME!")

    def test_rm(self, ):
        """>>>> Testing removing a file"""
        RemovalService.rm(self.tmpfilepath)
        # test that the file was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), msg="Failed to remove file")

    @patch("pysnips.py_utilities.mocking_sample.os")
    def test_rm_with_mock(self, mock_os):
        """>>>> Testing removing of file with mock"""
        RemovalService.rm("any path")
        # test that rm called os.remove with the right params
        mock_os.remove.assert_called_with("any path")

    @patch("pysnips.py_utilities.mocking_sample.os.path")
    @patch("pysnips.py_utilities.mocking_sample.os")
    def test_rm_after_validation(self, mock_os, mock_path):
        """>>>> Test to check if rm is validating path before delete"""
        mock_path.isfile.return_value = False

        RemovalService.rm("any path")

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called, "Failed to remove the file if not present")

        # make the file exist
        mock_path.isfile.return_value = True

        RemovalService.rm("any path")

        mock_os.remove.assert_called_with("any path")

    @patch("pysnips.py_utilities.mocking_sample.os.path")
    @patch("pysnips.py_utilities.mocking_sample.os")
    def test_rm_after_adding_service_class(self, mock_os, mock_path):
        """>>>> Testing rm function after making it a class method"""
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called, "Failed to remove the file if not present")

        # make the file exist
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
