Installation
============

Requirements
------------

* Python 3.11 or higher
* pip

From PyPI
---------

.. code-block:: bash

   pip install project-name

From Source
-----------

.. code-block:: bash

   git clone https://github.com/yourusername/project-name.git
   cd project-name
   pip install -e .

Development Installation
------------------------

.. code-block:: bash

   git clone https://github.com/yourusername/project-name.git
   cd project-name
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .[dev]