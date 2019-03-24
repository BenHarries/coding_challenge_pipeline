import unittest
import numpy as np
from random_transform import transform
from add_noise import add_noise


class TestPipelin(unittest.TestCase):

    def test_number_transform_image(self):
        image = np.random.randint(0, 255, size=(100, 100), dtype=np.uint8)
        for number_transforms in range(10):
            transformed_images = transform(image, 1, number_transforms)

            self.assertEqual(len(transformed_images), number_transforms)

    def test_add_noise(self):
        image = np.random.randint(0, 255, size=(5, 100, 100), dtype=np.uint8)

        print(image.shape)
        noisey_image = add_noise(image, 1, 40)

        image_sum = np.sum(image[0].reshape(100 * 100))
        noisey_image_sum = np.sum(noisey_image[0].reshape(100 * 100))

        self.assertNotEqual(image_sum, noisey_image_sum)


if __name__ == '__main__':
    unittest.main()
