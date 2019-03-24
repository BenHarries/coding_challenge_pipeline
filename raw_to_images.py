# code adapted from https://martin-thoma.com/classify-mnist-with-pybrain/

import imageio
from struct import unpack
import gzip
from numpy import zeros, uint8

def read_raw(path, outq):
    images = gzip.open(path, 'rb')

    # Read the binary data

    # We have to get big endian unsigned int. So we need '>I'

    # Get metadata for images
    images.read(4)  # skip the magic_number
    number_of_images = images.read(4)
    number_of_images = 5 # unpack('>I', number_of_images)[0]
    rows = images.read(4)
    rows = unpack('>I', rows)[0]
    cols = images.read(4)
    cols = unpack('>I', cols)[0]

    # Get the data
    x = zeros((number_of_images, rows, cols), dtype=uint8)
    # Initialize numpy array
    for i in range(number_of_images):
        print(i)
        if i % 1000 == 0:
            print("i: %i" % i)
        for row in range(rows):
            for col in range(cols):
                tmp_pixel = images.read(1)  # Just a single byte
                tmp_pixel = unpack('>B', tmp_pixel)[0]
                x[i][row][col] = tmp_pixel

        outq.put((x[i],i))

    # tell queue it has finished
    outq.put(None)
    return x

