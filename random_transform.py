# For each image in the dataset we want to create N new images
# where random transformations have been applied.

# The transformations are:
    # rotation from -100 to 100 degrees
    # following a uniform distribution translation

    # from -40% to 40% both axis following a uniform distribution

# The transformed images must be saved in a directory.

import imutils
import cv2
import numpy as np


def transform(data):
    img= data
    scale_max_x = 0.4
    scale_max_y = 0.4
    h, w = img.shape[:2]




