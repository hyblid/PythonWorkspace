'''
__init__.py is run when you IMPORT a package into a running python program. 
For instance, import idlelib within a program, runs idlelib/__init__.py,
which does not do anything as its only purpose is to mark the idlelib directory as a package.
On the otherhand, tkinter/__init__.py contains most of the tkinter code and defines all the widget classes.

__main__.py is run as '__main__' when you RUN a package as the main program. 
For instance, python -m idlelib at a command line runs idlelib/__main__.py, which starts Idle. Similarly, 
python -m tkinter runs tkinter/__main__.py, which has this line:

from . import _test as main
In this context, . is tkinter, so importing . imports tkinter, which runs tkinter/__init__.py. 
_test is a function defined within that file. 
So calling main() (next line) has the same effect as running python -m tkinter.__init__ at the command line.
'''