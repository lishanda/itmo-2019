# -*- coding: utf-8 -*-

import os
import shutil
import subprocess  # noqa S404
import unittest

import cats_composition_lishanda as cats_composition


class CatsCompositionTester(unittest.TestCase):
    """Cats_composition tester."""

    def setUp(self):
        """SetUp."""
        self.temp = 'temp'
        self.count = 1
        if not os.path.exists(self.temp):
            os.mkdir(self.temp)

    def tearDown(self):
        """Tear Down test."""
        shutil.rmtree(self.temp)

    def test_main(self):
        """Main test."""
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

        assert os.path.exists(fact_file)
        assert os.stat(fact_file).st_size != 0

    def test_integration(self):
        """Test func."""
        format_str = 'python cats_composition_lishanda.py {0}'  # noqa E800
        arg = '--count=1'
        command_str = format_str.format(arg)
        assert subprocess.call(command_str, shell=True) == 0  # noqa: S602, E501


if __name__ == '__main__':
    unittest.main()
