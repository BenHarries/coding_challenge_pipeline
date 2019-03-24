import numpy as np
import imageio


def add_noise(images, i, noise_param=60):
    for j, image in enumerate(images):
        noise = noise_param * np.random.normal(size=image.shape)
        print(noise)
        noise = noise.astype(int)

        noisy_image = image + noise

        imageio.imwrite('/Users/ben/code/ML/CCGpipeline/output/' + str(i) + '-' + str(j) + '.png', noisy_image)
    return noisy_image
