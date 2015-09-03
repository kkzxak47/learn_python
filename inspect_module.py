import platform
import inspect
import os
import sys

def module_viewer(module):
    """
    public methods and members of a module
    """
    print module.__name__
    print "="*20
    for name, member in filter(lambda tpl: not tpl[0].startswith('_'),
                               inspect.getmembers(module)):
        if module.__name__ == 'os' and name == 'abort':
            continue
        try:
            print "{}: {}".format(name, member())
        except Exception as e:
            print "{}: {}  ({})".format(name, str(member), e.message)

if __name__ == '__main__':
    module_viewer(platform)
    module_viewer(os)
    module_viewer(sys)
    module_viewer(inspect)
