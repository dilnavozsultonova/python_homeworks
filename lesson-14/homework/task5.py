import numpy  as np
from PIL import Image 
with Image.open("lesson-14/homework/images/birds.jpg") as img:
    img_arr=np.array(img)

def save_img(imgr,name,mode="L"):
    img2=Image.fromarray(imgr,mode)
    img2.save("lesson-14/homework/images/"+name)


flipped=img_arr[::-1]
save_img(flipped,"flipped.jpg","RGB")

rndm = np.random.randint(low=0, high=50, size=img_arr.shape)
@np.vectorize
def add(a, b):
    a += b
    return min(255, a)

noisy = add(img_arr, rndm).astype(np.int8)
save_img(noisy, "noisy.jpg", "RGB")

adding = np.array([40,0,0])
brightened_red = add(img_arr, adding).astype(np.int8)
save_img(brightened_red, "brightened_red.jpg","RGB")

new_arr = img_arr
new_arr[100:200, 100:200] = np.array([0,0,0])
save_img(new_arr, "mask.jpg", "RGB")