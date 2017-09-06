======
PyInit
======

PyInit is a simple script to ease the creation of projects for Python.
Supported Python versions: 3.5+

-----
Usage
-----

You should specify the paths to the directories templates and projects via
environment variables: PY_INIT_PROJECTS, PY_INIT_TEMPLATES.

.. code::

        $ git clone https://github.com/artcom-net/PyInit.git
        $ cd PyInit
        $ python py_init.py

Output:

.. code::

        >> Project name: Foo
        >> Create project dir: /home/dev/projects/Foo
        >> Create virtualenv: /home/dev/projects/Foo/venv
        >> Create file: .gitignore
        >> Create file: LICENSE
        >> Create file: MANIFEST.in
        >> Create file: README.rst
        >> Create file: requirements.txt
        >> Create file: setup.py
        >> Create dir: tests
        >> Create git repository

