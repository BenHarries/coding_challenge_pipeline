# code adapted from https://stackoverflow.com/questions/40427435/extract-images-from-idx3-ubyte-file-or-gzip-via-python

import gzip
import imageio

def read_raw(path='train-images-idx3-ubyte.gz'):

    f = gzip.open(path, 'r')

    image_size = 28
    num_images = 4

    import numpy as np
    f.read(16)
    buf = f.read(image_size * image_size * num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(num_images, image_size, image_size, 1)

    # import matplotlib.pyplot as plt
    image = np.asarray(data[0]).squeeze()
    file = '/Users/ben/code/ML/CCGpipeline/image.png'
    imageio.imwrite(file , image)

    return data

read_raw()