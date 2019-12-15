# -*- coding: utf-8 -*-

"""Module for self-testing of runtests framework."""

import os

import runtests


def test_load_correct_module():
    """Test load_module function with correct filepath."""
    assert runtests.load_module(
        os.path.join(os.getcwd(), 'students/lishanda/1/runtests.py'),
    )


def test_load_absent_module():
    """Test load_module function with incorrect input."""
    assert runtests.load_module('') is None
    assert runtests.load_module('filename.py') is None
    assert runtests.load_module('{0}/dont_test_me.py'.format(
        os.getcwd(),
    )) is None


def test_get_tests_from_module():
    """Test get_tests_from_module function."""
    module = runtests.load_module(
        os.path.join(os.getcwd(), 'students/lishanda/1/runtests.py'),
    )
    assert runtests.get_tests_from_module(module) is not None
    assert runtests.get_tests_from_module(None) is None


def test_files_from_path():
    """Test files_from_path function."""
    assert runtests.files_from_path('students/lishanda/1/', r'*.py')
    assert runtests.files_from_path('students/lishanda/1/', r'*')
    assert runtests.files_from_path('students/lishanda/1/', r'') is not None
