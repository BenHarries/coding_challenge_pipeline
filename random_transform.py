# For each image in the dataset we want to create N new images
# where random transformations have been applied.

# The transformations are:
    # rotation from -100 to 100 degrees
    # following a uniform distribution translation

    # from -40% to 40% both axis following a uniform distribution

# The transformed images must be saved in a directory.
# adapted from https://stackoverflow.com/questions/44401085/how-to-scale-the-image-along-x-and-y-axis-and-crop-to-a-specific-height-and-widt
import imutils
import imageio
import cv2
import numpy as np


def transform(img, N):
    for i in N:
        scale_x = np.random.uniform(-0.4,0.4) + 1
        scale_y = np.random.uniform(-0.4,0.4) + 1
        h, w = img.shape[:2]
        print(scale_y,scale_x)

        if scale_x > 1 or scale_y > 1:

            scaled_img = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)  # scale image
            sh, sw = scaled_img.shape[:2]  # get h, w of scaled image
            center_y = int(sh / 2 - h / 2)
            center_x = int(sw / 2 - w / 2)
            cropped = scaled_img[center_y:center_y + h, center_x:center_x + w]

            result = cropped

        elif scale_x > 0 or scale_y > 0:
            scaled_img = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_CUBIC)  # scale image
            result = scaled_img

        else:  # scale_x or scale_y is negative
            print("Scales must be greater than 0; returning the original image.")
            result = img

        # if result.shape < img.shape:  # one of the dimensions was scaled smaller, so need to pad
        #     sh, sw = result.shape[:2]  # get h, w of cropped, scaled image
        #     center_y = int(h / 2 - sh / 2)
        #     center_x = int(w / 2 - sw / 2)
        #     padded_scaled = np.zeros(img.shape, dtype=np.uint8)
        #     padded_scaled[center_y:center_y + sh, center_x:center_x + sw] = result
        #     result = padded_scaled
        # angle = np.random.uniform(-100,100)
        # image_center = tuple(np.array(image.shape[1::-1]) / 2)
        # rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        # result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        imageio.imwrite('/Users/ben/code/ML/CCGpipeline/transform' + str(i) + '.png', result)

    return result




transform()