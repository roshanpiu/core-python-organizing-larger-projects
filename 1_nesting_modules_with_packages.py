# Module is the python's basic tool for organizing code
# Module typically corresponds to a single source file
# Load module with the import keyword
# Represented by module objects
# Package is a special type of a module
# Package can contain other modules or other packages that contain modules

# Many parts of python's standard library is implemented as packages

import urllib
import urllib.request

# In this case urllib is a package and urllib.request is a module
print(type(urllib))
print(type(urllib.request))

# Importing a sub-module from a package
# Saying this will only bind request to a name in the local namespace
from urllib import request

# urllib has a __path__ member and urllib.request does not
# __path__ indicates where urllib searches to find nested modules
print(urllib.__path__)
print(urllib.request.__path__)

# Packages are generally directories and modules are generally files
