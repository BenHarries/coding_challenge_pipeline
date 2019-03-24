from raw_to_images import read_raw
from random_transform import transform
from add_noise import add_noise

images = read_raw('/Users/ben/code/ML/CCGpipeline/train-images-idx3-ubyte.gz')

all_transformed = []

for i in range(len(images)):
    all_transformed.append(transform(images[i], i, 4))

for i in range(len(all_transformed)):
    add_noise(all_transformed[i], i)




