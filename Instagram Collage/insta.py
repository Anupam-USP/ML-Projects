import cv2
import matplotlib.pyplot as plt
import numpy as np

# Select any of your 5 images
top_left = cv2.imread('/home/anupam/Downloads/pikachu.jpg')
top_right = cv2.imread('/home/anupam/Downloads/bulbasour.jpg')
center = cv2.imread('/home/anupam/Downloads/jigglypuff.jpeg')
bottom_right = cv2.imread('/home/anupam/Downloads/squirtle.jpg')
bottom_left = cv2.imread('/home/anupam/Downloads/charizard.jpg')

rgb_top_left = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)
rgb_top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
rgb_center = cv2.cvtColor(center, cv2.COLOR_BGR2RGB)
rgb_bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)
rgb_bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)

rgb_tl = cv2.resize(rgb_top_left, (200, 200))
rgb_br = cv2.resize(rgb_bottom_right, (200, 200))
rgb_tr = cv2.resize(rgb_top_right, (200, 200))
rgb_bl = cv2.resize(rgb_bottom_left, (200, 200))
rgb_ctr = cv2.resize(rgb_center, (200, 200))

rgb_tl = cv2.copyMakeBorder(rgb_tl, 10, 10, 10, 10, 0)  # top-left
rgb_tr = cv2.copyMakeBorder(rgb_tr, 10, 10, 0, 10, 0)  # top-right
rgb_br = cv2.copyMakeBorder(rgb_br, 0, 10, 0, 10, 0)  # bottom-right
rgb_bl = cv2.copyMakeBorder(rgb_bl, 0, 10, 10, 10, 0)  # bottom-left
rgb_ctr = cv2.copyMakeBorder(rgb_ctr, 10, 10, 10, 10, 0)  # center

# print(plt.imshow(rgb_tl))
# print(plt.imshow(rgb_tr))
# print(plt.imshow(rgb_br))
# print(plt.imshow(rgb_bl))
# print(plt.imshow(rgb_ctr))
#
# area=(40,40,40,40)
# plt.axis("Off")

zero = np.zeros((430, 430, 3), int)

zero[0:220, 220:430] = rgb_tr
zero[220:430, 220:430] = rgb_br
zero[0:220, 0:220] = rgb_tl
zero[220:430, 0:220] = rgb_bl
zero[110:330, 110:330] = rgb_ctr

plt.imshow(zero)
plt.show()
