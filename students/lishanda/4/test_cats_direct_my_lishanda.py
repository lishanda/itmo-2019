# -*- coding: utf-8 -*-

import os
import shutil
import subprocess  # noqa S404
import unittest

import pytest

import cats_direct_lishanda as cats_direct

INDEX_STRING = 'index'
EXTENSION_STRING = 'extension'


class CatsDirectTester(unittest.TestCase):  # noqa WPS230
    """Tests for cats_direct."""

    def setUp(self):
        """Set Up test."""
        self.metadata = {INDEX_STRING: 1, EXTENSION_STRING: 'jpg'}
        self.test_cat_fact = 'Amazing cat fact'

        self.temp = 'temp'
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)

        self.test_fact_file = '{0}/cat_{1}_fact.txt'.format(
            self.temp,
            self.metadata[INDEX_STRING],
        )
        self.test_image = '{0}.{1}'.format(
            'students/lishanda/4/test_image',
            self.metadata[EXTENSION_STRING],
        )
        self.result_image = '{0}/cat_{1}_image.{2}'.format(
            self.temp,
            self.metadata[INDEX_STRING],
            self.metadata[EXTENSION_STRING],
        )

    def tearDown(self):
        """Tear Down test."""
        shutil.rmtree(self.temp)

    def test_parser(self):
        """Argument parsing test."""
        args = ['--count', '1']
        parsed = cats_direct.create_parser().parse_args(args)
        assert parsed.count == int(args[-1])

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """Cat fact fetching test."""
        fact = cats_direct.fetch_cat_fact()
        assert fact != ''

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """Cat image fetching test."""
        fetched = cats_direct.fetch_cat_image()
        assert fetched[0]
        assert int(fetched[1].headers['Content-length']) != 0

    def test_save_cat(self):
        """Cat saver test."""
        assert os.path.isfile(self.test_image)

        with open(self.test_image, 'rb') as test_image:
            cats_direct.save_cat(
                index=self.metadata[INDEX_STRING],
                fact=self.test_cat_fact,
                image=(self.metadata[EXTENSION_STRING], test_image),
            )

        assert os.path.isfile(self.test_fact_file)
        with open(self.test_fact_file, 'r') as fact_file:
            assert fact_file.read() == self.test_cat_fact

        assert os.path.isfile(self.result_image)
        with open(self.result_image, 'rb') as image_file:
            assert image_file.read()

    def test_integration(self):
        """Test func."""
        format_str = 'python students/lishanda/4/cats_direct_lishanda.py {0}'  # noqa E800
        arg = '--count=2'
        command_str = format_str.format(arg)
        assert subprocess.call(command_str, shell=True) == 0  # noqa: S602, E501


if __name__ == '__main__':
    unittest.main()
