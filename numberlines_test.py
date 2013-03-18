import unittest
import os
import shutil
import numberlines

class FileHandling(unittest.TestCase):
    test_dir = 'testfiles'
    input_files = (
        'hipsteripsum50.txt',
        'sonnet116.txt',
        'roman.py'
    )

    def setUp(self):
        os.makedirs(test_dir, exist_ok=True)
        for input_file in input_files:
            shutil.copy(input_file, test_dir)

    def tearDown(self):
        shutil.rmtree(test_dir)

    def test_creates_file(self):
        '''should create a file with _numbered appended to its name'''
        for input_file in input_files:
            numberlines.number(test_dir + '/' + input_file)

class Numbering(unittest.TestCase):
    def test_no_arguments(self):
