# -*- coding: utf-8 -*-

import pytest  # noqa I003
import subprocess  # noqa S404

from cli import contains, ls, mk, rm, since

YES_THIS_IS_MAGIC_NUMBER = 123
TXT_FILENAME = 'file.txt'
INV_ARG = 'wrong argument'
PYSTR = 'python3'
CLISTR = 'cli.py'
DIRSTR = 'dir'
TXTSTR = ''


def mkdir(directory):
    """Mkdir func."""
    directory.mkdir()


def test_ls_empty_dir(tmp_path):
    """Test ls_empty_dir."""
    assert not ls(tmp_path)


def test_ls_only_dirs(tmp_path):
    """Test ls_only_dirs."""
    directory = tmp_path / 'another_dir'
    mkdir(directory)
    assert len(ls(tmp_path)) == 1


def test_ls_only_files(tmp_path):
    """Test ls_only_files."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert filename.read_text() == TXTSTR
    assert len(ls(tmp_path)) == 1


def test_ls_files_and_dirs(tmp_path):
    """Test ls_files_and_dirs."""
    directory = tmp_path / 'sub'
    mkdir(directory)
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert len(ls(tmp_path)) == 2


def test_ls_integration():
    """Test ls_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'ls']) == 0


def test_mk_no_filename():
    """Test mk_no_filename."""
    assert mk() == INV_ARG


def test_mk_en_filename(tmp_path):
    """Test mk_en_filename."""
    filename = tmp_path / TXT_FILENAME
    assert mk(filename) == 'success'


def test_mk_ru_filename(tmp_path):
    """Test mk_ru_filename."""
    filename = tmp_path / 'файл.txt'
    assert mk(filename) == 'success'


def test_mk_integration():
    """Test mk_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'mk', TXT_FILENAME]) == 0


def test_mk_duplicate(tmp_path):
    """Test mk_duplicate."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert mk(filename) == 'file already exists'


def test_mk_invalid_filename(tmp_path):
    """Test mk_invalid_filename."""
    filename = tmp_path / 'f/1/l/e.txt'
    assert mk(filename) == 'invalid filename'


def test_rm_success(tmp_path):
    """Test rm_success."""
    filename = tmp_path / TXT_FILENAME
    filename.write_text(TXTSTR)
    assert rm(filename) == 'success'


def test_rm_dir(tmp_path):
    """Test rm_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)  # noqa WPS204
    assert rm(directory) == 'argument is dir'


def test_rm_fail(tmp_path):
    """Test rm_fail."""
    filename = tmp_path / 'someFILENAME'
    assert rm(filename) == 'file not found'


def test_rm_no_filename():
    """Test rm_no_filename."""
    assert rm() == INV_ARG


def test_rm_integration():
    """Test rm_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'rm', 'someFILENAME']) == 0


def test_contains_no_filename():
    """Test contains_no_filename."""
    assert contains() == INV_ARG


def test_contains_success():
    """Test contains_success."""
    mk(TXT_FILENAME)
    assert contains(TXT_FILENAME) == 0
    rm(TXT_FILENAME)


def test_contains_dir(tmp_path):
    """Test contains_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)  # noqa WPS204
    assert contains(directory) == 'argument is dir'


def test_contains_non_existing_file():
    """Test contains_non_existing_file."""
    assert contains('non_existing_FILENAME') == 1


def test_since_no_date():
    """Test since_no_date."""
    assert since() == INV_ARG


def test_contains_integration():
    """Test contains_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'contains', TXT_FILENAME]) == 0


@pytest.fixture
def earlier_than_now_timestamp():
    """Timestamp."""
    from datetime import datetime  # noqa WPS433
    return int(datetime.timestamp(datetime.now())) - 10


def test_since_not_existing_dir(tmp_path):
    """Test since_not_existing_dir."""
    directory = tmp_path / DIRSTR
    assert since(YES_THIS_IS_MAGIC_NUMBER, directory) == 'dir not found'


def test_since_empty_dir(tmp_path):
    """Test since_empty_dir."""
    directory = tmp_path / DIRSTR
    mkdir(directory)
    assert since(YES_THIS_IS_MAGIC_NUMBER, directory) == 'dir is empty'


def test_since_only_dirs(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_only_dirs."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    adirectory = directory / 'another dir'
    adirectory.mkdir()
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 1


def test_since_only_files(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_only_files."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    filename = directory / TXT_FILENAME
    filename.write_text('test')
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 1


def test_since_dirs_and_files(tmp_path, earlier_than_now_timestamp):  # noqa WPS442
    """Test since_dirs_and_files."""
    directory = tmp_path / DIRSTR
    directory.mkdir()
    subdir = directory / 'subdir'
    subdir.mkdir()
    filename = directory / TXT_FILENAME
    filename.write_text(TXTSTR)
    func_result = since(earlier_than_now_timestamp, directory)
    assert isinstance(func_result, list)
    assert len(func_result) == 2


def test_since_integration():
    """Test since_integration."""
    assert subprocess.call([PYSTR, CLISTR, 'since', '0']) == 0


def test_since_invalid_date():
    """Test since_invalid_date."""
    assert since('abcd') == INV_ARG
