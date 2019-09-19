# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import itmo.second.cats_direct as cats_direct


class CatsDirectTestter(unittest.TestCase):  # noqa WPS230
    """Tests for cats_direct."""

    def setUp(self):
        """setUp."""
        self.data = {'index': 1, 'extension': 'jpg'}
        self.test_cat_fact = 'Amazing cat fact'

        self.temp = 'temp'
        if (not os.path.exists(self.temp)):
            os.mkdir(self.temp)

        self.test_fact_file = '{0}/cat_{1}_fact.txt'.format(
            self.temp,
            self.data['index'],
        )
        self.test_image = '{0}.{1}'.format(
            'test_image',
            self.data['extension'],
        )
        self.result_image = '{0}/cat_{1}_image.{2}'.format(
            self.temp,
            self.data['index'],
            self.data['extension'],
        )

    def tearDown(self):
        """tearDown."""
        shutil.rmtree(self.temp)

    def test_parser(self):
        """Argument parser test."""
        args = ['--count', '1']
        parsed = cats_direct.create_parser().parse_args(args)
        self.assertEqual(parsed.count, int(args[-1]))

    def test_fetch_cat_fact(self):
        """Cat fact fetch test."""
        fact = cats_direct.fetch_cat_fact()
        self.assertNotEqual(fact, '')

    def test_fetch_cat_image(self):
        """Cat image fetch test."""
        fetched = cats_direct.fetch_cat_image()
        self.assertGreater(len(fetched[0]), 0)
        self.assertNotEqual(int(fetched[1].headers['Content-length']), 0)

    def test_save_cat(self):
        """Cat save test."""
        self.assertTrue(os.path.isfile(self.test_image))

        with open(self.test_image, 'rb') as test_image:
            cats_direct.save_cat(
                index=self.data['index'],
                fact=self.test_cat_fact,
                image=(self.data['extension'], test_image),
            )

        self.assertTrue(os.path.isfile(self.test_fact_file))
        with open(self.test_fact_file, 'r') as fact_file:
            self.assertEqual(fact_file.read(), self.test_cat_fact)

        self.assertTrue(os.path.isfile(self.result_image))
        with open(self.result_image, 'rb') as image_file:
            self.assertNotEqual(len(image_file.read()), 0)


if __name__ == '__main__':
    unittest.main()
