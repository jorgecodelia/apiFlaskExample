# app/test/test_app.py

import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)
