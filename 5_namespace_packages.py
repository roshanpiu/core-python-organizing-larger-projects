# Namespace packages are a machanism for splitting a single Python package
# Across multiple directories on disk
# Can't have __init__.py . this avoid package loading order conflicts

# Namespace packages discovery algorithm ex - package foo
# 1 - Scan each directory in sys.path
# 2 - If a direct called foo found that has __init__.py a normal package is imported
# 3 - If a normal package is not found but a foo directory is found that is imported
# 4 - Otherwise all matching directories contributes to a namespace package