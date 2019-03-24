
# How to use code
pip install imageio

# Design decisions made
1. I returned a the full array of all the images rather than a set as numpy arrays are not hashable
2. Used Gaussian noise to add to all of the images
3. I added the ability to control the noise with 'noise_param'

Remaining todo's