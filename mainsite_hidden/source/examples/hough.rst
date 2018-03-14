======================================
Hough Transform and Edge detection
======================================

**Itom** offers the full power of **Python 3** in combination with **OpenCV 3**.
All OpenCV functions can be easily used and the results are visualized and further processed (e.g. output to Matlab) in python.

Often, edge detection and noise reduction are first applied in order to perform further processing like the Hough transform.
The following image shows two often used versions for edge enhancement or edge detection: Laplacian filtering and the famous Canny filter.
More Info on how to code `Canny in Python <http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html>`_

.. image:: ..\\_static\\examples\\edge.jpg
    :alt: Edge detection
    :width: 80%
    :align: center

.. raw:: html

	<hr>

The next screenshot shows the application of the so-called Hough transform used to find (in this case: long) lines in a very noisy image.
For more information: `Hough Line Transform <http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html>`_

.. image:: ..\\_static\\examples\\hough.png
    :alt: Hough filtering
    :width: 50%
    :align: center

.. raw:: html

	<hr>



