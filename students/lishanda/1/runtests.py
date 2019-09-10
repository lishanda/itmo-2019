import os
import importlib.util
import glob
import traceback

EXTENSION_NOTATION = ".py"
PREFIX = "test_"


def load_module(target_file):
    file_name = os.path.basename(target_file).replace(EXTENSION_NOTATION, "")

    if len(file_name) == 0 or (not os.path.exists(target_file)):
        return None

    spec = importlib.util.spec_from_file_location(file_name, target_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_tests_from_module(module):
    if module is None:
        return None
    func_dict = dict(filter(lambda elem: elem[0].startswith(PREFIX), vars(module).items()))
    return func_dict


def get_files_from_path(target_path, mask):
    return glob.glob(f"{target_path}/{mask}", recursive=True)


def launch_testing(target_path="", verbose=True):
    # Activate verbose flag for traceback logging

    # If target path is empty current directory is used
    if len(target_path) == 0:
        target_path = os.getcwd()

    # Finding testing modules
    test_files = get_files_from_path(target_path, f"{PREFIX}*{EXTENSION_NOTATION}")

    for test_file in test_files:
        module = load_module(test_file)
        if module is None:
            continue

        # Running tests and logging results
        tests = get_tests_from_module(module)
        for test in tests.items():
            try:
                tb = ""
                test[1]()
                test_result = "ok"
            except AssertionError:
                test_result = "fail"
                tb = traceback.format_exc()
            print(f"{test_file} | {test[0]} - {test_result}")
            if verbose and len(tb) != 0:
                print(tb)


if __name__ == '__main__':
    path = input("Enter path to directory with testing modules\n*Leave blank to choose current directory*: ")
    launch_testing(path, verbose=False)
