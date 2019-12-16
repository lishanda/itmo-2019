# -*- coding: utf-8 -*-

import os
import shutil
import unittest
from argparse import ArgumentParser

import pytest

from itmo.second import cats_direct

INDEX = 1
IMG_EXT = 'jpg'


class CatsDirectTester(unittest.TestCase):  # noqa WPS230
    """Tests for cats_direct."""

    path = 'students/lishanda/2'
    temp = 'temp'
    dummy_img_path = '{0}/{1}.{2}'.format(path, 'dummy', IMG_EXT)
    dummy_fact = 'Amazing dummy fact'

    def setUp(self):
        """Set Up test."""
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)

        self.test_fact_file = 'temp/cat_{0}_fact.txt'.format(INDEX)
        self.test_img_file = 'temp/cat_{0}_image.{1}'.format(
            INDEX,
            IMG_EXT,
        )

    def tearDown(self):
        """Tearing Down test by deleting temporary resources."""
        shutil.rmtree(self.temp)

    def test_create_parser(self):
        """create_parser should return correct ArgumentParser."""
        parsed = cats_direct.create_parser()
        self.assertNotEqual(parsed, None)
        self.assertIsInstance(parsed, ArgumentParser)

    def test_parser_count(self):
        """create_parser should parse argument --count."""
        args = ['--count', '10']
        parsed = cats_direct.create_parser().parse_args(args)
        self.assertEqual(parsed.count, int(args[-1]))

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """fetch_cat_fact should load fact from network."""
        fact = cats_direct.fetch_cat_fact()
        self.assertNotEqual(fact, None)
        self.assertNotEqual(fact, '')
        self.assertIsInstance(fact, str)

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """fetch_cat_image should load image from network."""
        img = cats_direct.fetch_cat_image()
        self.assertNotEqual(img, None)
        self.assertNotEqual(int(img[1].headers['Content-length']), 0)

    def test_save_cat(self):
        """save_cat should save fact and image correctly."""
        self.assertTrue(os.path.isfile(self.dummy_img_path))

        with open(self.dummy_img_path, 'rb') as test_image:
            cats_direct.save_cat(
                index=INDEX,
                fact=self.dummy_fact,
                image=(IMG_EXT, test_image),
            )

        self.assertTrue(os.path.isfile(self.test_img_file))
        with open(self.test_img_file, 'rb') as image_file:
            self.assertNotEqual(len(image_file.read()), 0)

        self.assertTrue(os.path.isfile(self.test_fact_file))
        with open(self.test_fact_file, 'rb') as fact_file:
            fact = fact_file.read()
            self.assertNotEqual(fact, '')
            self.assertIsInstance(fact, bytes)
            self.assertEqual(len(fact), len(self.dummy_fact))


if __name__ == '__main__':
    unittest.main()
