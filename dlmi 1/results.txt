# Brain Tumor Segmentation using Thresholding

## Project Description
This project performs brain tumor segmentation on MRI images using classical image processing techniques.

Two thresholding methods are used:
- Otsu Thresholding
- Sauvola Thresholding

The dataset used is the LGG MRI Segmentation dataset.

## Methods

1. Select a tumor slice from a patient folder
2. Resize image and mask to 256x256
3. Convert mask to binary
4. Apply Otsu thresholding
5. Apply Sauvola thresholding
6. Evaluate using Dice and Jaccard metrics

## Evaluation Metrics

Dice Score  
Measures overlap between predicted mask and ground truth mask.

Jaccard Score  
Measures intersection over union between prediction and ground truth.

## Results

Otsu Dice: 0.0461  
Sauvola Dice: 0.0437  
Otsu Jaccard: 0.0236  
Sauvola Jaccard: 0.0223  

## Why Results Are Low

Classical thresholding methods perform poorly for brain tumor segmentation because:

- Tumor intensity overlaps with normal brain tissue
- MRI images have complex intensity distributions
- Tumors have irregular shapes
- Thresholding does not understand spatial context

Deep learning models such as U-Net perform significantly better for this task.

## How to Run

1. Install required libraries:

pip install opencv-python numpy scikit-image

2. Update dataset path inside the Python file.

3. Run:

python project_medical.py

## Dataset

LGG MRI Segmentation Dataset (Kaggle)
