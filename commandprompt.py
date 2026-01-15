Microsoft Windows [Version 10.0.26100.4946]
(c) Microsoft Corporation. All rights reserved.

C:\Users\anany>python --version
Python 3.13.2

C:\Users\anany>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello , world")
hello , world
>>> exit()

C:\Users\anany>cd C:\Users\anany\Desktop\50marks

C:\Users\anany\Desktop\50marks>python face_attendance
python: can't open file 'C:\\Users\\anany\\Desktop\\50marks\\face_attendance': [Errno 2] No such file or directory

C:\Users\anany\Desktop\50marks>py face_attendance
C:\Program Files\Python313\python3.13t.exe: can't open file 'C:\\Users\\anany\\Desktop\\50marks\\face_attendance': [Errno 2] No such file or directory

C:\Users\anany\Desktop\50marks>cd C:\Users\anany\Desktop\50marks

C:\Users\anany\Desktop\50marks>python face_attendance.py
OpenCV bindings requires "numpy" package.
Install it via command:
    pip install numpy
Traceback (most recent call last):
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\_core\__init__.py", line 23, in <module>
    from . import multiarray
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\_core\multiarray.py", line 10, in <module>
    from . import overrides
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\_core\overrides.py", line 7, in <module>
    from numpy._core._multiarray_umath import (
        add_docstring,  _get_implementing_args, _ArrayFunctionDispatcher)
ImportError: PyCapsule_Import could not import module "datetime"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\__init__.py", line 127, in <module>
    from numpy.__config__ import show_config
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
    ...<3 lines>...
    )
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\_core\__init__.py", line 49, in <module>
    raise ImportError(msg)
ImportError:

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.13 from "C:\Program Files\Python313\python.exe"
  * The NumPy version is: "2.2.4"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: PyCapsule_Import could not import module "datetime"


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\anany\Desktop\50marks\face_attendance.py", line 1, in <module>
    import cv2
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\cv2\__init__.py", line 11, in <module>
    import numpy
  File "C:\Users\anany\AppData\Roaming\Python\Python313\site-packages\numpy\__init__.py", line 132, in <module>
    raise ImportError(msg) from e
ImportError: Error importing numpy: you should not try to import numpy from
        its source directory; please exit the numpy source tree, and relaunch
        your python interpreter from there.

C:\Users\anany\Desktop\50marks>
C:\Users\anany\Desktop\50marks>python face_attendance.py
Attendance recorded for ananya.jpg at 2025-09-21 21:29:47.375659
