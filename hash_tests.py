import os
import sys
import unittest
from os.path import join, exists
from pathlib import Path
from unittest.mock import patch
from io import StringIO

from hash import create_user, delete_user, check_password

PASSWORD_DIR = "password"
ERR_MSG = "Incorrect username or password"

# Your existing functions here


class TestLoginSystem(unittest.TestCase):

    def setUp(self):
        # Create the 'password' directory if it doesn't exist
        Path(PASSWORD_DIR).mkdir(exist_ok=True)

    def tearDown(self):
        # Delete the 'password' directory and its contents
        if exists(PASSWORD_DIR):
            for file in os.listdir(PASSWORD_DIR):
                os.remove(join(PASSWORD_DIR, file))
            os.rmdir(PASSWORD_DIR)

    def test_create_user(self):
        create_user('test_user', 'test_password')
        self.assertTrue(exists(join(PASSWORD_DIR, 'test_user')))

    def test_check_password_correct(self):
        create_user('test_user', 'test_password')
        self.assertTrue(check_password('test_user', 'test_password'))

    def test_check_password_incorrect(self):
        create_user('test_user', 'test_password')
        self.assertFalse(check_password('test_user', 'wrong_password'))

    def test_delete_user_correct(self):
        create_user('test_user', 'test_password')
        delete_user('test_user')
        self.assertFalse(exists(join(PASSWORD_DIR, 'test_user')))

    def test_delete_user_non_existing(self):
        self.assertFalse(delete_user('non_existing_user'))


if __name__ == '__main__':
    unittest.main()
