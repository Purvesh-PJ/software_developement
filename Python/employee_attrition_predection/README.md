# IMAGE-BASED FIRE DETECTION

## Dataset of Images:

You’ll need a set of labeled images, divided into two categories:
- Fire (images that contain fire)
- No Fire (images without fire)
- Ensure you have a balanced dataset to avoid bias.

## Preprocessing:
- Resize all images to a uniform size (e.g., 128x128 or 224x224).
- Normalize pixel values to be between 0 and 1 by dividing by 255.
- Split your dataset into training, validation, and test sets.

## Model Design:
- A CNN (Convolutional Neural Network) is well-suited for image classification tasks. You could use a pre-trained model like VGG16 or ResNet50, or build a custom CNN.

## Training:
- Use your dataset to train the model with the images. The model should output a binary classification (Fire/No Fire).

## Evaluation:
- Once trained, evaluate the model’s accuracy, precision, recall, and F1-score on a test set.

## Prediction on New Images:
- After training, the model can be used to predict whether new images contain fire.

# FOLDER STRUCTURE
```
fire_detection_project/
│
├── data/
│   ├── train/
│   │   ├── fire/              # Images with fire for training
│   │   └── no_fire/           # Images without fire for training
│   ├── validation/
│   │   ├── fire/
│   │   └── no_fire/
│   └── test/
│       ├── fire/              # Images with fire for testing
│       └── no_fire/           # Images without fire for testing
│
├── models/
│   ├── cnn_model.h5           # Saved trained model
│   └── model_checkpoint/      # Model checkpoints (optional)
│
├── notebooks/
│   └── fire_detection.ipynb   # Jupyter notebook for training and evaluation
│
├── src/
│   ├── data_preprocessing.py  # Preprocessing and augmentation code
│   ├── train_model.py         # Code for model training
│   ├── test_model.py          # Code for model testing
│   └── utils.py               # Utility functions (e.g., for loading data)
│
├── requirements.txt           # Dependencies (TensorFlow, NumPy, etc.)
├── README.md                  # Project documentation
└── main.py                    # Optional: Script to predict fire in images
```