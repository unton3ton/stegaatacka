# python3 -m venv ATTAK
# source ATTAK/bin/activate

# pip install opencv-python
# pip install matplotlib

# https://unimatrixz.com/blog/latent-space-image-quality-with-entropy/

'''
What is entropy?

Entropy measures the level of uncertainty or randomness in a dataset. In information theory, entropy is often associated with the average amount of information needed to encode a message or data set.
Entropy in image processing?

Entropy measures an image’s information content used in image processing. A high entropy number denotes a complex image with a wide range of pixel values, whereas a low entropy value denotes a more straightforward, uniform image. 

Entropy can be used to assess an image’s quality or complexity and to find the most informative portions of an image for further processing or analysis.
'''


import numpy as np
import cv2
from scipy.stats import entropy
import matplotlib.pyplot as plot

image_path = 'JUPoUQ.jpg'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_bins = 128

hist, _ = np.histogram(gray_image.ravel(), bins=_bins, range=(0, _bins))

prob_dist = hist / hist.sum()
image_entropy = entropy(prob_dist, base=2)
print(f"Image Entropy {image_entropy} for {image_path}")

plot.hist(hist, density=1, bins=_bins)
plot.savefig(f'ImageEntropy_{image_path}.png')
plot.show()

'''
Image Entropy 6.884162225879558 for 1.png
Image Entropy 6.884168387506503 for new.png

Image Entropy 6.878406945299694 for tinne-7.jpeg
Image Entropy 6.878406945299694 for tinne-7-with-hidetext.jpeg

Image Entropy 3.639428204549869 for re2.png
Image Entropy 3.6975179459936514 for embedded_text.png
Image Entropy 3.713204815625096 for embedded_text.jpg
Image Entropy 4.8650606316696425 for embedded_img.png
Image Entropy 0.046919139587702725 for embedded_text1.png

Image Entropy 0.38195800357484044 for 7corupt.png

Image Entropy 0.8511453835607288 for watermark_qrcode.png
Image Entropy 0.96557866684501 for watermark_qrcode (2-я извлёк).png
Image Entropy 5.807410296979399 for watermark_qrcode()извлёк после телеги.jpg
'''