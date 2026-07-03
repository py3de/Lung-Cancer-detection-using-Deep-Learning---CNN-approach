# Lung-Cancer-Detection-using-Deep-Learning-s-CNN

Overview:
This repository contains a deep-learning model for the detection of lung cancer using X-ray images. The model is based on Convolutional Neural Networks (CNNs) and has been trained on a small dataset consisting of approximately 478 images for training and 106 images for validation. This README file provides an overview of the project, instructions for running the model, and other relevant information.
Note: You can also find trained model with .h5 extension along with the interface app.py in this repository.

Dataset:  
The dataset used for training and validation includes a collection of X-ray images of lung scans. The dataset is divided into two main subsets:

Training Dataset:  Approximately 478 X-ray images.
Validation Dataset: Approximately 106 X-ray images.
Please note that this dataset is relatively small, and the model's performance may improve with a larger and more diverse dataset. It is important to ensure that you have the necessary permissions and rights to use this dataset for research or testing purposes.

Model Architecture:  
The lung cancer detection model is built using Convolutional Neural Networks (CNNs), a type of deep learning architecture well-suited for image classification tasks. The architecture of the CNN model used in this project is as follows:

Input Layer: Accepts X-ray images of a predefined size.
Convolutional Layers: Multiple convolutional layers for feature extraction.
Pooling Layers: Max-pooling layers to reduce spatial dimensions.
Fully Connected Layers: Dense layers for classification.
Output Layer: Sigmoid activation function for binary classification (cancer or non-cancer).

Requirements:  
To run the lung cancer detection model, you will need the following dependencies:

Python 3.x
TensorFlow or PyTorch (whichever framework the model is built with)
NumPy
Matplotlib (for visualization)
Any additional libraries specified in the project
