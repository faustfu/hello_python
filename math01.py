# 1. Module:PIL(Pillow) is for processing pictures.
# 1. Module:matplotlib is for drawing math graph.

import matplotlib.pyplot as plot
import matplotlib.image as image

img = image.imread('runner.gif')
plot.imshow(img)
plot.show()