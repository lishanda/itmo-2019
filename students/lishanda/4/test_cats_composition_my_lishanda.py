# -*- coding: utf-8 -*-

import os
import pytest
import shutil
import subprocess  # noqa S404
import unittest

from cats_composition_lishanda import CatProcessor, main
from cats_direct_lishanda import fetch_cat_fact, fetch_cat_image, save_cat


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

    @pytest.mark.remote_data
    def test_main(self):
        """Main test."""
        fact_file = '{0}/cat_{1}_fact.txt'.format(self.temp, self.count)
        if os.path.exists(fact_file):
            os.remove(fact_file)

        cat_processor = CatProcessor(
            fetch_cat_fact,
            fetch_cat_image,
            save_cat,
        )
        main(
            self.count,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        assert os.path.exists(fact_file)
        assert os.stat(fact_file).st_size != 0

    def test_integration(self):
        """Test func."""
        format_str = 'python students/lishanda/4/cats_composition_lishanda.py {0}'  # noqa E800
        arg = '--count=1'
        command_str = format_str.format(arg)
        assert subprocess.call(command_str, shell=True) == 0  # noqa: S602, E501


if __name__ == '__main__':
    unittest.main()
