import platform
import sys

a = platform.python_version()
b = sys.version.split()[0]

print(a == b)


