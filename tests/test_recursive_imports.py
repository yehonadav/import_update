from import_update import update_imports_recursively
from tests import utils
from tests.models import try1


def test_recursive_imports():

    files = utils.clean_imports_recursively(try1.__file__)

    assert len(files) == 3
    print("found {} init files".format(len(files)))

    utils.assert_imports_are_clean(files)
    print("init files are clean")

    update_imports_recursively(try1.__file__)
    update_imports_recursively(try1.__file__)
    utils.assert_import_lines_did_not_duplicate(files)

    try1.pkg1.mod1.A.run()
    try1.pkg1.mod2.B.run()
    try1.pkg1.mod3.C.run()
    try1.pkg2.mod1.A.run()
    try1.pkg2.mod2.B.run()
    try1.pkg2.mod3.C.run()
    try1.mod3.C.run()
    try1.mod1.A.run()
    try1.mod2.B.run()
