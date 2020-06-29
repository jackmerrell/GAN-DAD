## image_resizer.py
# Importing required libraries

import os
import numpy as np
from PIL import Image

# Defining an image size and image channel
# We are going to resize all our images to 128x128 size
# Set image channels to 3 (RGB)

IMAGE_SIZE = 128
IMAGE_CHANNELS = 3
IMAGE_DIR = 'dataset_1/'

# Defining image dir path.
images_path = IMAGE_DIR

training_data = []

# Iterating over the images in directory and resize them
# Pillows resize method
print('resizing...')

for filename in os.listdir(images_path):
    path = os.path.join(images_path, filename)
    image = Image.open(path).resize((IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)

    training_data.append(np.asarray(image))

training_data = np.reshape(
    training_data, (-1, IMAGE_SIZE, IMAGE_SIZE, IMAGE_CHANNELS))
training_data = training_data / 127.5 - 1

print('saving file...')
np.save('cubism_data_1.npy', training_data)