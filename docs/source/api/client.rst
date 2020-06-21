==============
Deezepy Client
==============

You've entered the API Reference section, where you can find all available methods and types.

This page is about the Client, which is used for high-level methods and easy API calls


.. code-block:: python

    import deezepy

    client = deezepy.Client()

    track = client.get_track(760429392)
    print(f"The title is: {track.title}" 

-------
Details
-------

.. autoclass:: deezepy.Client()