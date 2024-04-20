# CubeSat Data Processing and Downlink

This repository houses the development work for Project Rapid, a three-bay CubeSat project under the Bruin Spacecraft Group at UCLA. The focus is on implementing efficient data processing and downlink strategies to manage the bandwidth constraints of satellite communication.

## Project Overview

Project Rapid aims to test and demonstrate data handling capabilities in a low Earth orbit environment, utilizing the Arducam 5MP Plus OV5642 camera module for capturing images. The primary challenge addressed by this repository is the compression of these images to reduce the data size for downlink.

## Image Compression Technique

The implemented solution utilizes Singular Value Decomposition (SVD) to compress the images captured by the CubeSat's onboard camera. This method provides a balance between image quality and compression ratio, crucial for the bandwidth-limited communication channels used in space.

### Usage

To use the compression script, ensure you have Python installed along with the required libraries:
- NumPy
- PIL (Pillow)
- scikit-image

Run the script with the desired image path and the number of singular values:
```bash
python compress_image.py path_to_your_image.jpg 50
