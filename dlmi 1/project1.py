import os
import cv2
import numpy as np
from skimage.filters import threshold_sauvola

# Dataset path
base_path = r"C:\Users\lenovo\Downloads\archive (1)\lgg-mri-segmentation\kaggle_3m"

# Get patient folder
all_items = os.listdir(base_path)

patient_folders = [
    f for f in all_items
    if os.path.isdir(os.path.join(base_path, f))
]

if len(patient_folders) == 0:
    print("No patient folders found")
    exit()

patient_folder = patient_folders[0]
patient_path = os.path.join(base_path, patient_folder)

# Find slice with tumor
files = os.listdir(patient_path)

image_files = sorted([f for f in files if "mask" not in f])
mask_files = sorted([f for f in files if "mask" in f])

image_path = None
mask_path = None

for img_file, m_file in zip(image_files, mask_files):
    temp_mask = cv2.imread(os.path.join(patient_path, m_file), 0)
    if temp_mask is not None and np.sum(temp_mask) > 0:
        image_path = os.path.join(patient_path, img_file)
        mask_path = os.path.join(patient_path, m_file)
        break

if image_path is None:
    print("No tumor slice found")
    exit()

# Load image and mask
image = cv2.imread(image_path, 0)
mask = cv2.imread(mask_path, 0)

if image is None or mask is None:
    print("Error loading files")
    exit()

image = cv2.resize(image, (256, 256))
mask = cv2.resize(mask, (256, 256))
mask = (mask > 127).astype(np.uint8)

# Otsu threshold
_, otsu = cv2.threshold(
    image, 0, 1,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Sauvola threshold
window_size = 25
sauvola_thresh = threshold_sauvola(image, window_size=window_size)
sauvola = (image > sauvola_thresh).astype(np.uint8)

# Metrics
def dice_score(y_true, y_pred):
    intersection = np.sum(y_true * y_pred)
    return (2.0 * intersection) / (np.sum(y_true) + np.sum(y_pred) + 1e-8)

def jaccard_score(y_true, y_pred):
    intersection = np.sum(y_true * y_pred)
    union = np.sum(y_true) + np.sum(y_pred) - intersection
    return intersection / (union + 1e-8)

otsu_dice = dice_score(mask, otsu)
sauvola_dice = dice_score(mask, sauvola)
otsu_jaccard = jaccard_score(mask, otsu)
sauvola_jaccard = jaccard_score(mask, sauvola)

print("Results")
print("Otsu Dice:", otsu_dice)
print("Sauvola Dice:", sauvola_dice)
print("Otsu Jaccard:", otsu_jaccard)
print("Sauvola Jaccard:", sauvola_jaccard)
