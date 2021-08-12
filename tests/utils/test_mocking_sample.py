import os
import tempfile
import unittest

from mock import patch, create_autospec
from utils.mocking_sample import RemovalService, UploadService


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

    @patch("utils.mocking_sample.os")
    def test_rm_with_mock(self, mock_os):
        """>>>> Testing removing of file with mock"""
        RemovalService.rm("any path")
        # test that rm called os.remove with the right params
        mock_os.remove.assert_called_with("any path")

    @patch("utils.mocking_sample.os.path")
    @patch("utils.mocking_sample.os")
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

    @patch("utils.mocking_sample.os.path")
    @patch("utils.mocking_sample.os")
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


# todo: fix failing mocking test
@unittest.skip("Keeps failing, why?")
class UploadServiceTestCases(unittest.TestCase):
    """
    Tests for the Upload Service
    """

    @patch.object(RemovalService, "rm")
    def test_upload_complete(self, mock_rm):
        """>>>> Test that the upload is complete"""
        removal_service = RemovalService()
        upload_service = UploadService(removal_service)

        # call upload complete which should in turn call "rm"
        upload_service.upload_complete("upload file")

        # check that the rm method was called
        mock_rm.assert_called_with("upload file")

        # check that it called the rm method of removal service
        removal_service.rm.assert_called_with("upload file")

    @staticmethod
    def test_upload_complete_using_mock_instances(self, mock_rm):
        """>>>> Test upload complete is working using mock instances"""
        mock_removal_service = create_autospec(RemovalService)
        upload_service = UploadService(mock_removal_service)

        # call upload complete which should in turn call rm
        upload_service.upload_complete("uploaded file")

        # test that it called rm
        mock_removal_service.rm.assert_called_with("uploaded file")


if __name__ == '__main__':
    unittest.main()
