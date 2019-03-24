
# How to use code
1. git clone this repo
1. cd into the folder and run the following commands
1. `pip install imageio`
1. `pip install numpy`
1. `pip install gzip`
1. start the pipeline with `python3 main.py`

The transformed images will be created in `only_transformed`.

The final transformed and noisey images will be created in `output`

# How to run the tests
1. `python3 test.py`

# Design decisions made
1. I returned a the full array of all the images rather than a set as numpy arrays are not hashable
2. Used Gaussian noise to add to all of the images
3. I added the ability to control the noise with 'noise_param'

Remaining todo's