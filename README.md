# Rice-Image-Dataset-CNN 



# 🍚 Rice Image Classification using CNN
This repository contains a project aimed at classifying different varieties of rice using a Convolutional Neural Network (CNN). The model is built with TensorFlow/Keras to accurately distinguish between different types of rice grains from images.

## 🚀 Project Overview
Rice grain classification is essential for quality control in agriculture. This project uses a CNN model to classify images of different types of rice, helping to automate the quality assessment process.

## ✨ Key Features:
Dataset: Contains images of multiple varieties of rice, including Basmati, Jasmine, Arborio, and others.
Model Architecture: A custom CNN built with TensorFlow, designed to capture distinctive features of each rice variety.
High Accuracy: The model is trained to achieve high classification accuracy with effective data augmentation techniques.
## 📁 Dataset
Classes: Multiple varieties of rice(DATASET)[https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset ].
Number of Images: 12,000+ high-resolution images.
Image Size: 256x256 pixels.
### 📈 Approach
Data Preprocessing: Image normalization and augmentation, including random rotations, flips, and zooms, to improve model robustness.
Model Building:
Designed a CNN architecture to effectively extract features from rice images.
Implemented different layers (convolutional, pooling, fully connected) to learn complex patterns.
Training & Evaluation:
Used 80% of the dataset for training and 20% for validation.
Monitored accuracy and loss to avoid overfitting.
## 🛠️ Tools & Libraries
Python: The main programming language.
TensorFlow & Keras: For building and training the CNN model.
OpenCV: For image preprocessing.
Matplotlib & Seaborn: To visualize training metrics and evaluate model performance.
##🎯 Results
The CNN model achieved an accuracy of 98% on the test dataset.
Detailed metrics such as precision, recall, and F1-score are provided to assess the performance of each clas
