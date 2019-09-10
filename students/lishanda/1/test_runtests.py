# This is module for self-testing of runtests framework


import os
import runtests


def test_load_module():
    assert runtests.load_module(os.getcwd() + "/dont_test_me.py") is not None
    assert runtests.load_module("") is None
    assert runtests.load_module("filename.py") is None


def test_get_tests_from_module():
    module = runtests.load_module(os.getcwd() + "/test_simple_operations.py")
    assert runtests.get_tests_from_module(module) is not None
    assert runtests.get_tests_from_module(None) is None


def test_get_files_from_path():
    assert len(runtests.get_files_from_path(os.getcwd(), "*.py")) > 0
    assert len(runtests.get_files_from_path(os.getcwd(), "*")) > 0
    assert runtests.get_files_from_path(os.getcwd(), "") is not None
