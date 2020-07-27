# When asked python to import a module python looks in the file system
# For the corresponding python source file and loads that code
# To look for that python check the path attribute of the standard sys module

import sys

print(sys.path)

# sys.path is a list of directories python searches in order from the list until a match is found
# If no matches are found an ImportError is raised

print(sys.path[0])

sys.path.append('new_module') # sys.path can be manipulated to add new locations to look for modules

# instructing python to where to look for packages setting the PYTHONPATH
# instead of manipulating sys.path we can add to PYTHONPATH
# set PYTHONPATH=path1;path2;path3