import imageio
from struct import unpack
import gzip
from numpy import zeros, uint8


def read_raw(path, outq):
    """
    Extracts the images from the mnist gz file

    code adapted from https://martin-thoma.com/classify-mnist-with-pybrain/
    :param path: Path to the mnist gz file
    :param outq: Queue to add the image numpy arrays to
    :return: Returns numpy array containing all images (for use in single process applications)
    """
    images = gzip.open(path, 'rb')

    images.read(4)  # skip the magic_number
    number_of_images = images.read(4)
    number_of_images = unpack('>I', number_of_images)[0]
    rows = images.read(4)
    rows = unpack('>I', rows)[0]
    cols = images.read(4)
    cols = unpack('>I', cols)[0]

    # Get the data
    x = zeros((number_of_images, rows, cols), dtype=uint8)
    # Initialize numpy array
    for i in range(number_of_images):
        if i % 1000 == 0:
            print("Read the first %i images" % i)
        for row in range(rows):
            for col in range(cols):
                tmp_pixel = images.read(1)  # Just a single byte
                tmp_pixel = unpack('>B', tmp_pixel)[0]
                x[i][row][col] = tmp_pixel

        outq.put((x[i], i))

    # tell queue it has finished
    outq.put(None)
    return x
