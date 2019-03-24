import numpy as np
import imageio


def add_noise(images, i, noise_param):
    """
    Takes a list of transformed images and adds noise to them
    :param images: The list of transformed images
    :param i: The index of the image
    :param noise_param: How noisey the image should be
    :return: List of noisey images
    """

    noisey_images = []
    for j, image in enumerate(images):
        noise = noise_param * np.random.normal(size=image.shape)
        print(noise)
        noise = noise.astype(int)

        noisey_image = image + noise
        noisey_image = np.clip(noisey_image, 0, 255)
        noisey_image = noisey_image.astype(np.uint8)
        print(noisey_image.shape)
        imageio.imwrite('./output/' + str(i) + '-' + str(j) + '.png', noisey_image)
        noisey_images.append(noisey_image)

    return noisey_images


def add_noise_mp(inq, noise_param):
    while True:
        val = inq.get()
        if val is None:
            break
        add_noise(val[0], val[1], noise_param)
