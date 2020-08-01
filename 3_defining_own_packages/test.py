# A package is nothing more than a directory containing __init__.py

from ..package_root import testFunc

testFunc()

# __all__ controls which attributes are imported when import * is used
__all__ = ['func1', 'func2']
# if __all__ not specified imports all public names
# __all__ must be a list of names each entry is a name to import