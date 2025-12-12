Usage
=====

Basic Usage
-----------

.. code-block:: python

   from project_name import YourClass
   
   obj = YourClass()
   result = obj.do_something()

Configuration
-------------

.. code-block:: python

   from project_name.config import config
   
   config.set(debug=True, log_level="DEBUG")

Environment Variables
---------------------

* DEBUG - Enable debug mode (default: false)
* LOG_LEVEL - Set logging level (default: INFO)
* DATA_DIR - Directory for data files