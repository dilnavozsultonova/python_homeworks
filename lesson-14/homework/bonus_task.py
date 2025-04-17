import numpy as np
from PIL import Image

with Image.open("lesson-14/homework/images/birds.jpg") as img:
    img_arr=np.array(img)

def flip_image(arr):
    reversed_arr=arr[::-1]
    return reversed_arr

def add(a,b):
    a+=b
    return min(255,a)

def add_noise(img_arr):
    rndm = np.random.randint(low=0, high=50, size=img_arr.shape)
    noisy = add(img_arr, rndm).astype(np.int8)
    return noisy

def brighten_channels(img_arr):
    adding = np.array([40,0,0])
    brightened_red = add(img_arr, adding).astype(np.int8)
    return brightened_red

def apply_mask(img_arr, low_row, high_row, low_column, high_column):
    img_arr[low_row:high_row, low_column:high_column] = np.zeros(3).astype(np.int8)
    return img_arr


