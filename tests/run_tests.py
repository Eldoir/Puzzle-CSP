import os
import importlib
import inspect

def run_tests():
    directory = os.path.dirname(os.path.abspath(__file__))
    files = [file for file in os.listdir(directory) if file.startswith("test_") and file.endswith(".py")]
    print(f'{len(files)} file(s) found')

    for file in files:
        print(f'--- Running tests for file: {file} ---')
        module_name = os.path.splitext(file)[0]
        module = importlib.import_module(module_name)
        importlib.reload(module)

        for name, obj in inspect.getmembers(module):
            if name.startswith("test_") and inspect.isfunction(obj):
                try:
                    obj()
                    print(f"Test {name}: OK")
                except Exception as e:
                    print(f"Test {name}: FAIL: {e}")

if __name__ == "__main__":
    run_tests()