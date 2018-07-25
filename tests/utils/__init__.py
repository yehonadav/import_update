import glob


def clean_imports_recursively(root_init):
    files = []
    for filename in glob.iglob(root_init.replace("__init__.py", "") + '/**', recursive=True):
        if filename.endswith("__init__.py"):
            open(filename, 'w').close()
            files.append(filename)
    return files


def assert_imports_are_clean(files):
    for file in files:
        with open(file, 'r') as f:
            assert len(f.readlines()) == 0


def assert_import_lines_did_not_duplicate(files):
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        all_line_exist = 0
        import_line_exist = 0

        for i in range(len(lines)):
            if lines[i].startswith('__all__'):
                all_line_exist += 1

            elif lines[i].startswith('from . import *'):
                import_line_exist += 1

        assert all_line_exist == 1
        assert import_line_exist == 1
