# -*- coding: utf-8 -*-

"""Module for self-testing of runtests framework."""

import os
import runtests


def test_load_module():
    """Test load_module function."""
    assert runtests.load_module('{0}/dont_test_me.py'.format(
        os.getcwd(),
    )) is None
    assert runtests.load_module('') is None
    assert runtests.load_module('filename.py') is None


def test_get_tests_from_module():
    """Test get_tests_from_module function."""
    module = runtests.load_module('{0}/test_simple_operations.py'.format(
        os.getcwd(),
    ))
    assert runtests.get_tests_from_module(module) is not None
    assert runtests.get_tests_from_module(None) is None


def test_files_from_path():
    """Test files_from_path function."""
    assert runtests.files_from_path(os.getcwd(), '*.py')
    assert runtests.files_from_path(os.getcwd(), '*')
    assert runtests.files_from_path(os.getcwd(), '') is not None
