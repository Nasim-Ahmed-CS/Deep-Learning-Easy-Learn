from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img = Image.open('R.jpg')

# Display the image using Matplotlib
plt.imshow(img)
plt.axis('off')
plt.show()
