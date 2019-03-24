import numpy as np
import imageio # to read files
import matplotlib.pyplot as plt
import os

# image = from the random_transform script

def add_noise(path):
    print(path)
    image = imageio.imread(path)

    image = image[:,:,:3]

    noise = 1 * image.max() * ((2 *np.random.random(image.shape)) -1)

    noise = noise.astype(int)

    noisy1 = image + noise
    return noisy1


folder = os.listdir("/Users/ben/code/ML/data")
for file in folder: # will not be getting files from here
    input_file = '/Users/ben/code/ML/CCGprep/data/input/' + file
    noisy_image = add_noise(input_file)
    plt.imshow(noisy_image)
    plt.show()
    file = '/Users/ben/code/ML/CCGprep/data/output/' + file
    imageio.imwrite(file , noisy_image)
