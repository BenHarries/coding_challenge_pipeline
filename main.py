from raw_to_images import read_raw
from random_transform import transform
# from add_noise import add_noise

images = read_raw('/Users/ben/code/ML/CCGpipeline/train-images-idx3-ubyte.gz')

for i in range(len(images)):
    transform(images[i], i, 4)


