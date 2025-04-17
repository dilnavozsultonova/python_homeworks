import numpy as np
from PIL import Image
with Image.open("lesson-14/homework/images/image.png") as img:
    img_arr=np.array(img)

imgg=(img_arr[:,:,0]*0.299+img_arr[:,:,1]*0.587+img_arr[:,:,2]*0.114).astype(np.int8)

img2=Image.fromarray(imgg,"L")
img2.save("lesson-14/homework/images/bird.jpg")

# \\text{Grayscale}=0.299R+0.587G+0.114B\n",