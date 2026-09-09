import matplotlib.image as mpimg
import matplotlib.pyplot as plt

file = "sagital.jpg"

image = mpimg.imread(file)

plt.imshow(image)

plt.axis("off")

plt.show()


