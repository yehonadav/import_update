# import_update
automatically update your pkg imports.

# simple usage
from import_update import update_imports_recursively
import your_dynamic_package

# this will update all init files under the root init directory
update_imports_recursively(your_dynamic_package.__file__)