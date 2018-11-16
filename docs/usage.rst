=====
Usage
=====

To use pyfb-customerportal in a project, add it to your `INSTALLED_APPS`:

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
