# code adapted from https://martin-thoma.com/classify-mnist-with-pybrain/

import imageio
from struct import unpack
import gzip
from numpy import zeros, uint8, float32

import numpy as np
import imageio
import cv2

def read_raw(path='train-images-idx3-ubyte.gz'):
    images = gzip.open(path, 'rb')

    # Read the binary data

    # We have to get big endian unsigned int. So we need '>I'

    # Get metadata for images
    images.read(4)  # skip the magic_number
    number_of_images = images.read(4)
    number_of_images = 100 # unpack('>I', number_of_images)[0]
    rows = images.read(4)
    rows = unpack('>I', rows)[0]
    cols = images.read(4)
    cols = unpack('>I', cols)[0]

    # Get the data
    x = zeros((number_of_images, rows, cols), dtype=float32)
    # Initialize numpy array
    for i in range(number_of_images):

        if i % 1000 == 0:
            print("i: %i" % i)
        for row in range(rows):
            for col in range(cols):
                tmp_pixel = images.read(1)  # Just a single byte
                tmp_pixel = unpack('>B', tmp_pixel)[0]
                x[i][row][col] = tmp_pixel
    # for i in range(1):
    #     print(x[i])
    #     imageio.imwrite('/Users/ben/code/ML/CCGpipeline/image' + str(i) +'.png',x[i])
    return x

