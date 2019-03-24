from raw_to_images import read_raw
from random_transform import transform, transform_mp
from add_noise import add_noise_mp
import multiprocessing as mp

PATH = './train-images-idx3-ubyte.gz'

NUMBER_OF_TRANSFORMS = 4
NOISE_PARAM = 60

transform_queue = mp.Queue()
noise_queue = mp.Queue()

read_worker = mp.Process(target=read_raw, args=(PATH, transform_queue))
transform_worker = mp.Process(target=transform_mp, args=(transform_queue, noise_queue, NUMBER_OF_TRANSFORMS))
add_noise_worker = mp.Process(target=add_noise_mp, args=(noise_queue, NOISE_PARAM))

read_worker.start()
transform_worker.start()
add_noise_worker.start()
read_worker.join()
transform_worker.join()
add_noise_worker.join()
