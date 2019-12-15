# -*- coding: utf-8 -*-

"""Framework for automatic test collection and running."""

import glob
import os
from importlib import util

EXT = '.py'
PREFIX = 'test_'


def load_module(target_file):
    """Load module for further testing."""
    file_name = os.path.basename(target_file).replace(EXT, '')

    if not file_name or (not os.path.exists(target_file)):
        return None

    spec = util.spec_from_file_location(file_name, target_file)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_tests_from_module(module):
    """Gather tests from loaded module."""
    if module is None:
        return None

    extracted_vars = vars(module).items()  # noqa: WPS421
    test_list = filter(lambda elem: elem[0].startswith(PREFIX), extracted_vars)
    return dict(test_list)


def files_from_path(target_path, mask):
    """Load files from specified folder."""
    mask_path = os.path.join(target_path, mask)
    return glob.glob(mask_path, recursive=True)


def test_test(test, test_file):
    """Test extracted testing function."""
    succeed = True
    try:
        test[1]()
    except AssertionError:
        succeed = False
    print('{0} | {1} - {2}'.format(  # noqa: T001
        test_file,
        test[0],
        'successful' if succeed else 'failed',
    ))


def launch_testing(path=''):
    """Load module for further testing."""
    # If target path is empty current directory is used
    if not path:
        path = os.getcwd()

    files = files_from_path(path, '{0}*{1}'.format(PREFIX, EXT))
    for t_file in files:
        if load_module(t_file) is None:
            continue

        # Running tests and logging results
        tests = get_tests_from_module(load_module(t_file))
        for test in tests.items():
            test_test(test, t_file)
