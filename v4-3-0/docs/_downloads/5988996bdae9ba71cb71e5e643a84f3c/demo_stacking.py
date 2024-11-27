"""Stacking arrays
==================
"""

import numpy as np

# sphinx_gallery_thumbnail_path = '11_demos/_static/_thumb/demoNumpy.png'

rg = np.random.default_rng(1)
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
np.vstack((a, b))

###############################################################################
np.hstack((a, b))

###############################################################################
np.column_stack((a, b))

###############################################################################
a[:, np.newaxis]

###############################################################################
np.column_stack((a[:, np.newaxis], b[:, np.newaxis]))

###############################################################################
np.column_stack is np.hstack

###############################################################################
np.row_stack is np.vstack