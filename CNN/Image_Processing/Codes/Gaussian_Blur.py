import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

class GaussianBlur(nn.Module):
    def __init__(self, kernel_size=5, sigma=1.0):
        super(GaussianBlur, self).__init__()
        self.kernel_size = kernel_size
        self.sigma = sigma

        # Create a Gaussian kernel
        self.kernel = self.create_gaussian_kernel(kernel_size, sigma)

        # Convert kernel to a PyTorch tensor
        self.kernel = torch.FloatTensor(self.kernel).unsqueeze(0).unsqueeze(0)

        # Define a 2D convolutional layer with a single input channel and a single output channel
        self.conv = nn.Conv2d(1, 1, kernel_size, padding=kernel_size//2, bias=False)

        # Set the convolutional layer's weights to the Gaussian kernel
        self.conv.weight.data = self.kernel
        # Disable gradient calculation for the convolutional layer since the kernel is fixed
        for param in self.conv.parameters():
            param.requires_grad = False

    def create_gaussian_kernel(self, kernel_size, sigma):
        # Create a 2D Gaussian kernel
        kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
        center = kernel_size // 2

        for i in range(kernel_size):
            for j in range(kernel_size):
                x, y = i - center, j - center
                kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))

        # Normalize the kernel
        kernel /= kernel.sum()
        return kernel

    def forward(self, x):
        # Apply the convolutional layer to the input image
        return self.conv(x)

# Example usage:
# Load your image and convert it to grayscale if necessary
# Then convert it to a PyTorch tensor
image = torch.randn(1, 1, 32, 32)  # Example random grayscale image
# Create a GaussianBlur instance
gaussian_blur = GaussianBlur(kernel_size=5, sigma=1.0)
# Apply Gaussian blur to the image
blurred_image = gaussian_blur(image)


blurred_image_numpy = blurred_image.squeeze(0).permute(1, 2, 0).numpy()

# Display the blurred image
plt.imshow(blurred_image_numpy, cmap='gray')
plt.axis('off')
plt.show()
