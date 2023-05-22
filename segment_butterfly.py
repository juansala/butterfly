import cv2
import matplotlib.pyplot as plt
import numpy as np

# TODO: Keep  track of HSVs from CV img
# TODO: Explore Color quantization without dithering

butterfly = cv2.imread('butterfly_nebula_reduced.png')
# butterfly = cv2.imread('red_square.png')
# butterfly = cv2.cvtColor(butterfly, cv2.COLOR_BGR2RGB)
# butterfly = cv2.cvtColor(butterfly, cv2.COLOR_RGB2HSV)
butterfly = cv2.cvtColor(butterfly, cv2.COLOR_BGR2HSV)

# TODO: Get low_res version
# butterfly_lo =
# (width, height, _) = butterfly.shape
# hsv_vals = []
# for i in range(width):
#     for j in range(height):
#         hsv = butterfly[i][j]
#         if not list(hsv) in hsv_vals:
#             print(hsv)
#             hsv_vals.append(list(hsv))
#             # print(butterfly[i][j])

# print(len(hsv_vals))

# HSV Ranges
hsv_ranges = {'layer1': {'lo': (140, 0, 0),
                         'hi' : (170, 255, 255)},
              'layer2': {'lo': (142, 0, 0),
                         'hi': (179, 255, 184)},
              'layer3': {'lo': (0, 95, 65),
                         'hi' : (179, 255, 255)},
              'layer4': {'lo': (0, 136, 0),
                         'hi': (179, 255, 95)}
                         }

masks = []
for layer in hsv_ranges.values():
    new_mask = cv2.inRange(butterfly, layer['lo'], layer['hi'])
    output = cv2.bitwise_and(butterfly,butterfly, mask=new_mask)
    masks.append(output)

num_plots = len(masks) + 1
plt.subplot(1, num_plots, 1)
plt.imshow(butterfly)
cv2.imwrite('complete.png', butterfly)
for i, mask in enumerate(masks):
    plt.subplot(1, num_plots, i+2)
    plt.imshow(mask, cmap='gray')
    cv2.imwrite('layer{:d}.png'.format(i), mask)

plt.show()