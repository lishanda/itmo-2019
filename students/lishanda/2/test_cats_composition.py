# -*- coding: utf-8 -*-

import os
import unittest

import cats_composition


class CatsCompositionTester(unittest.TestCase):
    """Cats_composition tester."""

    def setUp(self):
        """SetUp."""
        self.temp = 'temp'
        self.count = 1

    def test_main(self):
        """Main test."""
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)

        fact_file = '{0}/cat_{1}_fact.txt'.format(self.temp, self.count)
        if os.path.exists(fact_file):
            os.remove(fact_file)

        cat_processor = cats_composition.CatProcessor(
            cats_composition.fetch_cat_fact,
            cats_composition.fetch_cat_image,
            cats_composition.save_cat,
        )
        cats_composition.main(
            self.count,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(fact_file))
        self.assertNotEqual(os.stat(fact_file).st_size, 0)


if __name__ == '__main__':
    unittest.main()
