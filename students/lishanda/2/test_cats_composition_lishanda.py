# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import pytest

from itmo.second import cats_composition

INDEX = 1
IMG_EXT = 'jpg'


class CatsCompositionTester(unittest.TestCase):
    """Cats_composition tester."""

    temp = 'temp'
    test_fact_file = '{0}/cat_{1}_fact.txt'.format(temp, INDEX)

    def setUp(self):
        """Setting up test by creating temp folder."""
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)

    def tearDown(self):
        """Tearing Down test by deleting temporary resources."""
        shutil.rmtree(self.temp)

    @pytest.mark.remote_data
    def test_main(self):
        """Testing main function."""
        if os.path.exists(self.test_fact_file):
            os.remove(self.test_fact_file)

        cat_processor = cats_composition.CatProcessor(
            cats_composition.fetch_cat_fact,
            cats_composition.fetch_cat_image,
            cats_composition.save_cat,
        )
        cats_composition.main(
            INDEX,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(self.test_fact_file))
        self.assertNotEqual(os.stat(self.test_fact_file).st_size, 0)


if __name__ == '__main__':
    unittest.main()
