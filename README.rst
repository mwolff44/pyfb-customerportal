=============================
pyfb-customerportal
=============================

.. image:: https://badge.fury.io/py/pyfb-customerportal.svg
    :target: https://badge.fury.io/py/pyfb-customerportal

.. image:: https://travis-ci.org/mwolff44/pyfb-customerportal.svg?branch=master
    :target: https://travis-ci.org/mwolff44/pyfb-customerportal

.. image:: https://codecov.io/gh/mwolff44/pyfb-customerportal/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mwolff44/pyfb-customerportal

Customer portal for PyFreeBilling project

Documentation
-------------

The full documentation is at https://pyfb-customerportal.readthedocs.io.

Quickstart
----------

Install pyfb-customerportal::

    pip install pyfb-customerportal

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pyfb_customerportal.apps.PyfbCustomerportalConfig',
        ...
    )

Add pyfb-customerportal's URL patterns:

.. code-block:: python

    from pyfb_customerportal import urls as pyfb_customerportal_urls


    urlpatterns = [
        ...
        url(r'^', include(pyfb_customerportal_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
