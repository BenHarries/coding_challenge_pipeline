import numpy as np
import imageio


def add_noise(images, i, noise_param):
    for j, image in enumerate(images):
        noise = noise_param * np.random.normal(size=image.shape)
        print(noise)
        noise = noise.astype(int)

        noisy_image = image + noise

        imageio.imwrite('/Users/ben/code/ML/CCGpipeline/output/' + str(i) + '-' + str(j) + '.png', noisy_image)
    return noisy_image

def add_noise_mp(inq, noise_param):
    while True:
        val=inq.get()
        if val is None:
            break
        add_noise(val[0], val[1], noise_param)