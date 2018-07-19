# -*- coding: utf-8 -*-
import unittest

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    if size < 0:
        raise ValueError(f'Número "{size}" inválido')
    else:
        if size > 0:
            if a_kilobyte_is_1024_bytes:
                return '931.3 GiB'
            return '1.0 TB'
        else:
            if a_kilobyte_is_1024_bytes:
                return '0 KB'
            return '0 KiB'


def approximate_size(size, a_kilobyte_is_1024_bytes = True):

    if size < 0:
        raise ValueError(f'Número "{size}" inválido')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{:.1f} {}'.format(size, suffix)
        
    
class TestApproximateSize(unittest.TestCase):

    def test_error_in_invalid_value_argument_size(self):
        with self.assertRaises(ValueError):
            value = approximate_size(-1)

    def test_success_approximate_size_with_size_zero_and_argument_default_true(self):
        self.assertEqual(approximate_size(0), '0.0 KiB')

    def test_success_approximate_size_with_size_zero_and_argument_default_false(self):
        self.assertEqual(approximate_size(0, False), '0.0 KB')

    def test_success_approximate_size_with_argument_default_false(self):
        value = approximate_size(1000000000000, False)
        self.assertEqual(value, '1.0 TB')

    def test_success_approximate_size_with_argument_default_true(self):
        value = approximate_size(1000000000000)
        self.assertEqual(value, '931.3 GiB')

    def test_sucess_approximate_size_success_with_argument_false(self):
        value = approximate_size(1000, False)
        self.assertEqual(value, '1.0 KB')


if __name__ == '__main__':
    unittest.main()
    
