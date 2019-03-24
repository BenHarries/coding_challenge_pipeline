# For each image in the dataset we want to create N new images
# where random transformations have been applied.

# The transformations are:
# rotation from -100 to 100 degrees
# following a uniform distribution translation

# from -40% to 40% both axis following a uniform distribution

# The transformed images must be saved in a directory.
# adapted from https://stackoverflow.com/questions/44401085/how-to-scale-the-image-along-x-and-y-axis-and-crop-to-a-specific-height-and-widt
import imutils
import imageio
import cv2
import numpy as np
from scipy import ndimage


def transform(image, filename, N):
    all_transformed = []
    for j in range(N):
        # rotate
        angle = np.random.uniform(-100, 100)
        rotated = ndimage.rotate(image, angle)

        # translate
        h, w = rotated.shape
        scaled_h = h * np.random.uniform(-.4, .4)
        scaled_w = w * np.random.uniform(-.4, .4)
        translated_image = ndimage.interpolation.shift(rotated, (scaled_h, scaled_w))

        all_transformed.append(translated_image)

        imageio.imwrite('/Users/ben/code/ML/CCGpipeline/only_transformed/' + str(filename) + '-' + str(j) + '.png',
                        translated_image)

    return all_transformed


def transform_mp(inq, outq, number_transforms):
    while True:
        val = inq.get()
        print("got image to transform")
        if val is None:
            outq.put(None)
            break

        transformed_images = transform(val[0], val[1], number_transforms)
        outq.put((transformed_images, val[1]))
