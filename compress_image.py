# Compressing images captured by the Arducam 5MP Plus OV5642 for CubeSat project
# 
# Developed by Kevin Lee, UCLA Aerospace M.S., kevinlee69720@g.ucla.edu
# https://github.com/magnaprog/CubeSat-Data-Procressing-and-Downlink
# 
# Bruin Spacecraft Group

import numpy as np
from PIL import Image
from skimage import img_as_float
from numpy.linalg import svd

def compress_image(image_path, k):
    """
    Compresses the given image using Singular Value Decomposition (SVD).

    Parameters:
        image_path (str): The path to the input image.
        k (int): The number of singular values to keep for compression.

    Returns:
        PIL.Image.Image: The compressed image.
    """
    # Load the image
    img = Image.open(image_path)
    img = img.convert('L')  # Convert to grayscale
    img_array = img_as_float(img)

    # Perform SVD
    U, s, V = svd(img_array, full_matrices=False)

    # Select k singular values/components
    U = U[:, :k]
    s = s[:k]
    V = V[:k, :]

    # Reconstruct the image
    S = np.diag(s)
    compressed_img = np.dot(U, np.dot(S, V))

    # Convert back to image
    compressed_img = Image.fromarray((compressed_img * 255).astype(np.uint8))
    compressed_img.save('compressed_image.jpg')
    return compressed_img

# Example usage
compress_image('path_to_your_image.jpg', 50)  # Compress using the top 50 singular values
