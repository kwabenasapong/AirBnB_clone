#!/usr/bin/python3
'''Unittest for file_storage'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class Test_FileStorage(unittest.TestCase):
    """Class to Test FileStorage"""
    data = FileStorage()
    client = BaseModel()

    def test_new(self):
        '''Test for new attr'''
        self.assertIs(self.data.new(self.client), None)

    def test_all(self):
        '''Test for all attr'''
        self.data.new(self.client)
        self.data.save()
        all = self.data.all()
        self.assertEqual(self.data.all(), all)

    def test_save(self):
        '''Test for save attr'''
        self.data.new(self.client)
        self.data.save()
        file_path = os.path.abspath("file.json")
        self.assertTrue(os.path.exists(file_path))
        self.assertIs(self.data.save(), None)

    def test_reload(self):
        '''Test for reload attr'''
        self.data.new(self.client)
        self.assertIs(self.data.reload(), None)


if __name__ == "__main__":
    unittest.main()
